# Local Serverless

It's very common to have serverless on any cloud based services. Nevertheless,
have you ever tried to build your own "Serverless" application! That's possible
and this repository shows how.

## How to use it?

Feel free to use this repository as you wish, there is a makefile to help
running some commands.

1. Installing the dependencies: The only ones wich is necessary is the ones to
run the fastapi. Install it using `make install`.

2. Start the application with `make start`.

You will see the api running, but not much memory being used. Even though the
applications listed on layers are going to be built, ran and return the result,
causing the container to be dropped.
