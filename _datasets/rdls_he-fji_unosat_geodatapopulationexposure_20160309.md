---
attributions:
- entity:
    affiliation: null
    email: null
    name: Joint Typhoon Warning Center
    url: https://data.humdata.org/dataset/geodata-of-population-exposure-analysis-tropical-cyclone-winston-22-february-march-09-2016
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-population-exposure-analysis-tropical-cyclone-winston-22-february-march-09-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-population-exposure-analysis-tropical-cyclone-winston-22-february-march-09-2016
dataset_id: rdls_he-fji_unosat_geodatapopulationexposure_20160309
description: 'Population exposure estimates based on observed cyclone track and sustained
  wind speeds of more than 90 Km/h and 120 Km/h ( 22 February 2016, Joint Typhoon
  Warning Center). [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-population-exposure-analysis-tropical-cyclone-winston-22-february-march-09-2016]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population exposed to tropical cyclone wind speeds exceeding 90 km/h
      and 120 km/h thresholds
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
  - analysis_type: probabilistic
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
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts integrated observed cyclone track and sustained wind
    speed data from the Joint Typhoon Warning Center to delineate areas experiencing
    wind speeds exceeding 90 km/h and 120 km/h thresholds. Population exposure was
    estimated by overlaying these wind speed zones with gridded population data to
    quantify the population at risk from tropical cyclone winds.
  sources:
  - id: source_1
    license: null
    name: Joint Typhoon Warning Center
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-population-exposure-analysis-tropical-cyclone-winston-22-february-march-09-2016
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Fiji - Geodata of Population Exposure Analysis - Tropical Cyclone Winston
    - 22 February 2016 (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/FJ/TC20160219FJI/TC20160219FJI_shp.zip
  format: null
  id: resource_839fd610
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20160219FJI_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Fiji - Geodata of Population Exposure Analysis - Tropical Cyclone Winston
    - 22 February 2016 (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/FJ/TC20160219FJI/TC20160219FJI.gdb.zip
  format: null
  id: resource_df81e9ee
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20160219FJI.gdb.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-fji_unosat_geodatapopulationexposure_20160309
spatial:
  bbox: null
  centroid: null
  countries:
  - FJI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-03-09'
temporal_resolution: null
title: Fiji - Geodata of Population Exposure Analysis - Tropical Cyclone Winston -
  22 February 2016
version: null
vulnerability: null
---
