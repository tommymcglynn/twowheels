#!/bin/bash

if pgrep httpd > /dev/null; then exit 0; else exit 1; fi