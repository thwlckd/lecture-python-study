/*
// PyCppExt.cpp - PyBind11-based Python Cpp Extension 

#include <pybind11/pybind11.h>
#include <string>
#include <pybind11/numpy.h> 

using namespace std;

namespace py = pybind11;

static string probe(void)
{
	return "PyCppExt.probe() was invoked";
}

PYBIND11_MODULE(PyCppExt, m)
{
	m.doc() = "pybind11 PyCppExt plugin"; // optional module docstring
	m.def("probe", &probe, "A function to check module existence");
}
*/



// PyCppExt.cpp - PyBind11-based Python Cpp Extension (1)
#include <pybind11/pybind11.h>
#include <string>
#include <pybind11/numpy.h> 

using namespace std;

namespace py = pybind11;

static string probe(void)
{
	return "PyCppExt.probe() was invoked";
}

template <typename T>
T add(T i, T j)
{
	return i + j;
}

template <typename T>
T mul(T x, T y)
{
	return x * y;
}


// PyCppExt.cpp - PyBind11-based Python Cpp Extension (2)
template <typename T>
py::array_t<T> add_arrays(py::array_t<T> input1, py::array_t<T> input2)
{
	py::buffer_info buf1 = input1.request(), buf2 = input2.request();

	if (buf1.ndim != 1 || buf2.ndim != 1)
		throw std::runtime_error("Number of dimensions must be one");

	if (buf1.size != buf2.size)
		throw std::runtime_error("Input shapes must match");

	// No pointer is passed, so NumPy will allocate the buffer
	auto result = py::array_t<T>(buf1.size);

	py::buffer_info buf3 = result.request();

	T* ptr1 = static_cast<T*>(buf1.ptr);
	T* ptr2 = static_cast<T*>(buf2.ptr);
	T* ptr3 = static_cast<T*>(buf3.ptr);

	for (size_t idx = 0; idx < buf1.shape[0]; idx++)
		ptr3[idx] = ptr1[idx] + ptr2[idx];

	return result;
}

// PyCppExt.cpp - PyBind11-based Python Cpp Extension (3)
template <typename T>
py::array_t<T> sort_array(py::array_t<T> array)
{
	py::buffer_info buf = array.request();

	if (buf.ndim != 1)
		throw std::runtime_error("Number of dimensions must be one");

	T* ptr = static_cast<T*>(buf.ptr);
	int idx_min;
	T min, temp;

	for (size_t i = 0; i < buf.shape[0]; i++)
	{
		idx_min = i;
		min = ptr[idx_min];
		for (size_t j = i + 1; j < buf.shape[0]; j++)
		{
			if (ptr[j] < min)
			{
				idx_min = j;
				min = ptr[idx_min];
			}
		}
		if (idx_min != i)
		{
			temp = ptr[i];
			ptr[i] = ptr[idx_min];
			ptr[idx_min] = temp;
		}
	}

	return array;
}

// PyCppExt.cpp - PyBind11-based Python Cpp Extension (4)
template <typename T>
py::array_t<T> mtrx_add(py::array_t<T> input1, py::array_t<T> input2)
{
	py::buffer_info buf1 = input1.request(), buf2 = input2.request();

	if (buf1.ndim != 2 || buf2.ndim != 2)
		throw std::runtime_error("Number of dimensions must be two");

	if (buf1.size != buf2.size)
		throw std::runtime_error("Input shapes must match");

	// No pointer is passed, so NumPy will allocate the buffer
	auto result = py::array_t<T>(buf1.shape[0] * buf2.shape[1]);

	py::buffer_info buf3 = result.request();

	T* ptr1 = static_cast<T*>(buf1.ptr);
	T* ptr2 = static_cast<T*>(buf2.ptr);
	T* ptr3 = static_cast<T*>(buf3.ptr);
	int row_size = buf1.shape[0];
	int col_size = buf2.shape[1];
	for (size_t r = 0; r < row_size; r++)
		for (size_t c = 0; c < col_size; c++)
		{
			ptr3[r * col_size + c] = ptr1[r * col_size + c] + ptr2[r * col_size + c];
		}

	return result;
}

// PyCppExt.cpp - PyBind11-based Python Cpp Extension (4)
PYBIND11_MODULE(PyCppExt, m)
{
	m.doc() = "pybind11 PyCppExt plugin"; // optional module docstring

	m.def("probe", &probe, "A function to check module existence");
	m.def("add", &add<int>, "A function which adds two numbers");
	m.def("add", &add<double>, "A function which adds two numbers");
	m.def("mul", &mul<int>, "A function which multiply two numbers");
	m.def("mul", &mul<double>, "A function which multiply two numbers");
	m.def("add_arrays", &add_arrays<int>, "Add two int arrays");
	m.def("add_arrays", &add_arrays<double>, "Add two double arrays");
	m.def("sort_array", &sort_array<int>, "Sort int array");
	m.def("sort_array", &sort_array<double>, "Sort double array");
}


/*
#include <pybind11/pybind11.h>
#include <string>
#include <pybind11/numpy.h> 

using namespace std;

namespace py = pybind11;

static string probe(void)
{
	return "PyCppExt.probe() was invoked";
}

template <typename T>
void m_sort(T list[], T l, T m, T r)
{
	T i, j, k;
	i = l;
	j = m + 1;
	k = l;
	T temp[11];

	while (i <= m && j <= r)
	{
		if (list[i] <= list[j])
			temp[k++] = list[i++];
		else
			temp[k++] = list[j++];
	}
	if (i > m)
	{
		for (T x = j; x <= r; x++)
			temp[k++] = list[x];
	}
	else
	{
		for (T x = i; x <= m; x++)
			temp[k++] = list[x];
	}

	for (T x = l; x <= r; x++)
		list[x] = temp[x];
}

template <typename T>
void merge(T list[], T l, T r)
{
	T mid;
	if (l < r)
	{
		mid = (l + r) / 2;
		merge(list, l, mid);
		merge(list, mid + 1, r);
		m_sort(list, l, mid, r);
	}
}

template <typename T>
py::array_t<T> sort_array(py::array_t<T> array)
{
	py::buffer_info buf = array.request();

	if (buf.ndim != 1)
		throw std::runtime_error("Number of dimensions must be one");

	T* ptr = static_cast<T*>(buf.ptr);
	int idx_min;
	T min, temp;

	for (size_t i = 0; i < buf.shape[0]; i++)
	{
		idx_min = i;
		min = ptr[idx_min];
		for (size_t j = i + 1; j < buf.shape[0]; j++)
		{
			if (ptr[j] < min)
			{
				idx_min = j;
				min = ptr[idx_min];
			}
		}
		if (idx_min != i)
		{
			temp = ptr[i];
			ptr[i] = ptr[idx_min];
			ptr[idx_min] = temp;
		}
	}

	return array;
}

PYBIND11_MODULE(PyCppExt, m)
{
	m.doc() = "pybind11 PyCppExt plugin"; // optional module docstring

	m.def("probe", &probe, "A function to check module existence");
	m.def("m_sort", &m_sort<int>, "A function which adds two numbers");
	//m.def("add", &m_sort<double>, "A function which adds two numbers");
	m.def("merge", &merge<int>, "A function which multiply two numbers");
	//m.def("mul", &merge<double>, "A function which multiply two numbers");
}
*/