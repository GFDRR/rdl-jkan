---
attributions:
- entity:
    affiliation: null
    email: null
    name: Global Risk Modelling Alliance
    url: https://grma.global
  id: attribution_publisher_001
  role: publisher
- entity:
    affiliation: null
    email: null
    name: AXA Climate
    url: https://climate.axa
  id: attribution_creator_001
  role: creator
- entity:
    affiliation: null
    email: baptiste.ronfard@axaclimate.com
    name: AXA Climate
    url: https://climate.axa
  id: attribution_contact_point_001
  role: contact_point
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Global Risk Modelling Alliance
  url: https://grma.global
creator:
  affiliation: null
  email: null
  name: Global Risk Modelling Alliance
  url: https://grma.global
dataset_id: rdls_hzd-mdg_grma_locusthabitatsuitabilitym
description: This map has been produced by training a random forest model using bioclimatic
  variables, sand concentration in soil, elevation and landcover features ; and locust
  larvae observations from the Locust Hub in the North East of Africa. Maps are available
  for the baseline (1995-2014), 2050 SSP2-4.5, 2050 SSP5-8.5, 2085 SSP2-4.5 and 2085
  SSP5-8.5.
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: GRMA Madagascar - Phase 1
  url: https://www.resiliencemada.gov.mg
publisher:
  affiliation: null
  email: null
  name: Global Risk Modelling Alliance
  url: https://grma.global
purpose: This dataset was developed during the first phase of GRMA's project in Madagascar.
  This project aimed at updating Madagascar's risk profile, and see the risk evolution
  under climate change.
referenced_by: []
resources:
- access_url: https://www.worldclim.org
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Bioclimatic variables downscaled at 30 arcsec for present and future
    climate from 6 CMIP6 models
  download_url: null
  format: GeoTIFF
  id: resource_worldclim2
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal: null
  temporal_resolution: null
  title: WorldClim 2 Bioclimatic Variables
- access_url: https://doi.org/10.17027/isric-soilgrids/e70d9b3b-a395-4cf7-a6f9-06ca316e506c
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Sand content mass fraction in per mille at 6 standard depths, resampled
    to 1000m
  download_url: null
  format: GeoTIFF
  id: resource_soilgrids
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal: null
  temporal_resolution: null
  title: SoilGrids250m 2.0 - Sand Content
- access_url: https://locust-hub-hqfao.hub.arcgis.com
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Desert locust observation data from FAO. Nymphs in North West Africa
    used to train the random forest model.
  download_url: null
  format: GeoJSON
  id: resource_locust_hub
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FAO Locust Hub - Larvae Observations
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mdg_grma_locusthabitatsuitabilitym
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Locust habitat suitability map
version: '1.0'
vulnerability: null
---
