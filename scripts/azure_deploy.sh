#!/bin/bash

az webapp config container set \
  --name docopsapp10sagar \
  --resource-group docops \
  --docker-custom-image-name 10sagar/docops
