#!/bin/sh

echo "... loading virtualenv ..."
. ${PROJECT_DIR}/python-env/bin/activate

cd ${PROJECT_DIR}
echo "... installing requirements ..."
pip install ${WHEEL}
${BINARY}
