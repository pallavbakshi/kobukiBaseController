#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/pb/kobuki_pallav/src/kobuki_controller_main"

# snsure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/pb/kobuki_pallav/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/pb/kobuki_pallav/install/lib/python2.7/dist-packages:/home/pb/kobuki_pallav/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/pb/kobuki_pallav/build" \
    "/usr/bin/python" \
    "/home/pb/kobuki_pallav/src/kobuki_controller_main/setup.py" \
    build --build-base "/home/pb/kobuki_pallav/build/kobuki_controller_main" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/pb/kobuki_pallav/install" --install-scripts="/home/pb/kobuki_pallav/install/bin"
