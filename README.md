# ISOXML library for python 

a python library that handles import and export of ISOXML TaskData files as specified in ISO11783 part 10.
inspired by [isoxml-js](https://github.com/dev4Agriculture/isoxml-js) and powered by [xsdata](https://github.com/tefra/xsdata) XML bindings.

The main features:
* supports v3 and v4
* read/write directly from zip, TASKDATA-dir or any string
* conversion between shapely and isoxml geometries
* conversion of numpy array to grid data binary files
* [generate code](./examples/pycode_generator.py) from existing TASKDATA.XML (via xsdata)

## Installation
```
pip install isoxml
```

## Usage Examples

### import

```python
from isoxml.util.isoxml_io import isoxml_from_zip

task_data, bin_data = isoxml_from_zip('/path/to/TASKDATA.zip')
```

### export

```python
import isoxml.models.base.v4 as iso
from isoxml.util.isoxml_io import isoxml_to_text

customer = iso.Customer(
    id="CTR0001",
    last_name="demo_customer"
)
farm = iso.Farm(
    id="FRM0001",
    designator="demo farm",
    customer_id_ref=customer.id
)
task_data = iso.Iso11783TaskData(
    management_software_manufacturer="josephinum research",
    management_software_version="0.0.0",
    data_transfer_origin=iso.Iso11783TaskDataDataTransferOrigin.FMIS,
    customers=[customer],
    farms=[farm]
)

xml_content = isoxml_to_text(task_data)

print(xml_content)
```

```xml
<ISO11783_TaskData VersionMajor="4" VersionMinor="3" ManagementSoftwareManufacturer="josephinum research" ManagementSoftwareVersion="0.0.0" DataTransferOrigin="1">
    <CTR A="CTR0001" B="demo_customer"/>
    <FRM A="FRM0001" B="demo farm" I="CTR0001"/>
</ISO11783_TaskData>
```

### more

[see examples](./examples)

## Dependencies

* [xsdata](https://github.com/tefra/xsdata) - Naive XML Bindings for python.
* [shapely](https://github.com/shapely/shapely) - a widely used library for editing and analyzing geometric objects.
* [numpy](https://github.com/numpy/numpy) - you know it, you love it