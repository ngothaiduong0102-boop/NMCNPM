#!/usr/bin/env bash
pytest -q --maxfail=1 --disable-warnings --html=report_unit.html --self-contained-html
