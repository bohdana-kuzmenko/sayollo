# Sayollo

App is build according to DDD architecture principles

**Domain** layer has base entities
 - request entity
 - sdk
 - user

And repositories interfaces

**Infrastructure** layer contains implementation of domain repos
As a test example there was decided to have sqllight solution as temporary one.
Better approaches:
 - store request data to same persistent relational db and counts tables have to be stored to memory db like Redis or Memcached
 - store all the data to timeseries db like Druid (looks like better decision)

**Application** layer contains services, and flask application

All the repos and services are initialized in main.py

Such app architecture allows you to create flexible solution that allows you to switch between different solutions on any layer with minimal effort, f.ex use different data storages, or replace flask with any other framework

