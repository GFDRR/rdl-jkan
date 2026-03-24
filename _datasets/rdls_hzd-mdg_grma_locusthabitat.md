---
catalog: null
contact_point:
  email: baptiste.ronfard@axaclimate.com
  id: attribution_contact_point_001
  name: AXA Climate
  url: https://climate.axa
creator:
  email: null
  id: attribution_creator_001
  name: AXA Climate
  url: https://climate.axa
dataset_id: rdls_hzd-mdg_grma_locusthabitat
description: This map has been produced by training a random forest model using bioclimatic
  variables, sand concentration in soil, elevation and landcover features ; and locust
  larvae observations from the Locust Hub in the North East of Africa. Maps are available
  for the baseline (1995-2014), 2050 SSP2-4.5, 2050 SSP5-8.5, 2085 SSP2-4.5 and 2085
  SSP5-8.5.
details: null
exposure: []
extra_attributions: []
hazard: null
license: CC-BY-4.0
loss: null
project:
  name: GRMA Madagascar - Phase 1
  url: https://www.resiliencemada.gov.mg
publisher:
  email: null
  id: attribution_publisher_001
  name: Global Risk Modelling Alliance
  url: https://grma.global
purpose: This dataset was developed during the first phase of GRMA's project in Madagascar.
  This project aimed at updating Madagascar's risk profile, and see the risk evolution
  under climate change.
resources:
- coordinate_system: EPSG:4326
  description: Bioclimatic variables downscaled at 30 arcsec for present and future
    climate from 6 CMIP6 models
  download_url: https://www.worldclim.org
  format: GeoTIFF (tif)
  id: resource_worldclim2
  media_type: null
  spatial_resolution: 1000
  temporal: null
  title: WorldClim 2 Bioclimatic Variables
- coordinate_system: EPSG:4326
  description: Sand content mass fraction in per mille at 6 standard depths, resampled
    to 1000m
  download_url: https://doi.org/10.17027/isric-soilgrids/e70d9b3b-a395-4cf7-a6f9-06ca316e506c
  format: GeoTIFF (tif)
  id: resource_soilgrids
  media_type: null
  spatial_resolution: 1000
  temporal: null
  title: SoilGrids250m 2.0 - Sand Content
- coordinate_system: null
  description: Desert locust observation data from FAO. Nymphs in North West Africa
    used to train the random forest model.
  download_url: https://locust-hub-hqfao.hub.arcgis.com
  format: GeoJSON (geojson)
  id: resource_locust_hub
  media_type: null
  spatial_resolution: null
  temporal: null
  title: FAO Locust Hub - Larvae Observations
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-mdg_grma_locusthabitat
spatial:
  countries:
  - MDG
  scale: national
title: Locust habitat suitability map
version: '1.0'
vulnerability: null
---
