@echo off

REM Makefile for Sphinx documentation (Windows batch version)

if "%1" == "" goto help

if "%1" == "help" (
	:help
	echo.Please use `make ^<target^>` where ^<target^> is one of
	echo.  html       to make standalone HTML files
	echo.  clean      to remove build files
	goto end
)

if "%1" == "clean" (
	rmdir /s /q build
	echo.Build files cleaned.
	goto end
)

if "%1" == "html" (
	sphinx-build -M html source build
	echo.
	echo.Build finished. The HTML pages are in build\html\.
	goto end
)

:end
