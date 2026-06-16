---
attributions:
- entity:
    affiliation: null
    email: null
    name: INGC (National Disaster Management Authority of Mozambique)
    url: https://data.humdata.org/dataset/aerial-survey-idai-24-29-march-2019
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IFRC
    url: https://data.humdata.org/dataset/aerial-survey-idai-24-29-march-2019
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNDAC
    url: https://data.humdata.org/dataset/aerial-survey-idai-24-29-march-2019
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: MapAction
    url: https://data.humdata.org/dataset/aerial-survey-idai-24-29-march-2019
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Federation of Red Cross and Red Crescent Societies (IFRC)
  url: https://data.humdata.org/dataset/aerial-survey-idai-24-29-march-2019
creator:
  affiliation: null
  email: null
  name: International Federation of Red Cross and Red Crescent Societies (IFRC)
  url: https://data.humdata.org/dataset/aerial-survey-idai-24-29-march-2019
dataset_id: rdls_hel-moz_ifrc_cycloneidaiaerialsurvey_201903
description: 'This data relates to an aerial survey conducted of Mozambique from the
  24-29 March 2019 following tropical cyclone Idai. Data was collected by INGC (National
  Disaster Management Authority of Mozambique), IFRC, UNDAC, MSF, DFID, Save the Children,
  and MapAction. Enumerators flew in squirrel helicopters over priority areas (usually
  at 500 feet) and some fixed wing aircraft for confirmation on outlying areas. Data
  contains location, points of interest, severity and estimated population. The survey
  used Kobo for data collection. Processing was conducted in R and then imported into
  ArcGIS for final map products. Data is presented in .xlsx (with and without hxl
  tags) and .geojson formats.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/aerial-survey-idai-24-29-march-2019]'
details: This data relates to an aerial survey conducted of Mozambique from the 24th
  to the 29th of March 2019 following cyclone Idai. It was collected by INGC (National
  Disaster Management Authority of Mozambique), IFRC, UNDAC, MSF, DFID, Savethechildren,
  and MapAction. The survey used Kobo for data collection and were conducted mostly
  using squirrel helicopters and some fixed wing aircraft. The data contains the location,
  severity, estimated population. Processing was conducted in R and then imported
  into ArcGIS for final map products.
exposure:
- asset_type:
    description: Estimated population in surveyed areas affected by cyclone Idai
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Aerial survey data collected via helicopter and fixed-wing aircraft
    over priority areas in Mozambique from 24-29 March 2019 following tropical cyclone
    Idai. Enumerators recorded location, points of interest, severity assessments,
    and estimated population using Kobo data collection tools. Data was processed
    in R and imported into ArcGIS for spatial analysis and validation.
  sources:
  - id: source_1
    license: null
    name: INGC (National Disaster Management Authority of Mozambique)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: IFRC
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: UNDAC
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: MapAction
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/aerial-survey-idai-24-29-march-2019
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Estimated affected population from aerial survey observations of
      cyclone Idai impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique - Cyclone Idai - Aerial Survey (Aerial survey data in GeoJSON
    format)
  download_url: https://data.humdata.org/dataset/50e37b45-25a1-4ef4-8c83-8b2fdf923773/resource/9584ef21-2151-468e-94a8-49864b62c70b/download/moz_cycloneidaiaerialsurvey.geojson
  format: null
  id: resource_9584ef21
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_cycloneidaiaerialsurvey.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique - Cyclone Idai - Aerial Survey (Aerial survey data in XLSX
    format with HXL tags)
  download_url: https://data.humdata.org/dataset/50e37b45-25a1-4ef4-8c83-8b2fdf923773/resource/05d6134c-1234-4857-982c-a9ccf42711d8/download/moz_cycloneidai_aerialsurvey_hxl.xlsx
  format: null
  id: resource_05d6134c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_cycloneidai_aerialsurvey_hxl.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique - Cyclone Idai - Aerial Survey (Aerial survey data in XLSX
    format with HXL tags)
  download_url: https://data.humdata.org/dataset/50e37b45-25a1-4ef4-8c83-8b2fdf923773/resource/1600f1a5-7db3-41a0-ab66-0d12f97b9653/download/moz_cycloneidai_aerialsurvey.xlsx
  format: null
  id: resource_1600f1a5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_cycloneidai_aerialsurvey.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data captured during an aerial survey of area affected by TC Idai,
    Mozambique. The survey was organised and implemented by INGC (Govt of Mozambique),
    IFRC and UNDAC. Data was cleaned and visualised by MapAction.
  download_url: https://data.humdata.org/dataset/50e37b45-25a1-4ef4-8c83-8b2fdf923773/resource/740855a4-aee4-41f1-b991-9a59f3da2a6c/download/moz_idai_aerialsurvey.zip
  format: null
  id: resource_740855a4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_Idai_AerialSurvey.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique - Cyclone Idai - Aerial Survey (Shapefile)
  download_url: https://data.humdata.org/dataset/50e37b45-25a1-4ef4-8c83-8b2fdf923773/resource/1e2912cc-feb8-475d-99f0-f6f05563e2a2/download/moz_cycloneidai_arealsurvey.zip
  format: null
  id: resource_1e2912cc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_cycloneidai_arealsurvey
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-moz_ifrc_cycloneidaiaerialsurvey_201903
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-03-29'
  start: '2019-03-24'
temporal_resolution: null
title: Mozambique - Cyclone Idai - Aerial Survey
version: null
vulnerability: null
---
