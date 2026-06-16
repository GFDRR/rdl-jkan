---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNDAC Team - Disaster Management Dept. Tanzania
    url: https://data.humdata.org/dataset/affected-and-wards-by-10-october-2016-eathquake
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: MapAction
  url: https://data.humdata.org/dataset/affected-and-wards-by-10-october-2016-eathquake
creator:
  affiliation: null
  email: null
  name: MapAction
  url: https://data.humdata.org/dataset/affected-and-wards-by-10-october-2016-eathquake
dataset_id: rdls_lss-tza_mapaction_affectedwards10october201_20160926
description: 'Affected wards, 10 October 2016 earthquake. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/affected-and-wards-by-10-october-2016-eathquake]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event affected ward boundaries were delineated by the UNDAC Team
    and Tanzanian Disaster Management Department using direct observational and anecdotal
    data collected in the immediate aftermath of the 10 October 2016 earthquake. Ward-level
    administrative polygons from TNBS/OCHA were attributed with affected status to
    create a spatial inventory of earthquake impact.
  sources:
  - id: source_1
    license: null
    name: UNDAC Team - Disaster Management Dept. Tanzania
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/affected-and-wards-by-10-october-2016-eathquake
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by the 10 October 2016 earthquake in Tanzania,
      mapped at ward administrative level
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: Tanzania affected wards, 10 October 2016 earthquake. (Shapefile)
  download_url: https://data.humdata.org/dataset/10957fd9-4aac-4e0a-bac7-5122c8271911/resource/33bd1497-057c-4310-8666-aa68b32b55ae/download/tza_admn_ad3_py_s1_wards_tnbs_ocha_.zip
  format: null
  id: resource_33bd1497
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_admn_ad3_py_s1_wards_TNBS_OCHA_.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-tza_mapaction_affectedwards10october201_20160926
spatial:
  bbox: null
  centroid: null
  countries:
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-09-26'
temporal_resolution: null
title: Tanzania affected wards, 10 October 2016 earthquake.
version: null
vulnerability: null
---
