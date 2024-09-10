automatically generated using [xsdata](https://github.com/tefra/xsdata)

```bash
xsdata resources/xsd/ISO11783_TaskFile_V3-3.xsd \
        --package isoxml.models.base.v3 \
        --subscriptable-types \
        --union-type \
        --structure-style clusters \
        --no-relative-imports
        
for filename in ./isoxml/models/base/v3/*.py; do
  python ./isoxml/models/refactor_helper.py $filename
done

xsdata resources/xsd/ISO11783_TaskFile_V4-3.xsd \
        --package isoxml.models.base.v4 \
        --subscriptable-types \
        --union-type \
        --structure-style clusters \
        --no-relative-imports 
        
for filename in ./isoxml/models/base/v4/*.py; do
  python ./isoxml/models/refactor_helper.py $filename
done
```