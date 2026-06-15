---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flood-impact-to-cropland-in-nairobi-and-kiambu-county-kenya-as-of-1-may-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-to-cropland-in-nairobi-and-kiambu-county-kenya-as-of-1-may-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-to-cropland-in-nairobi-and-kiambu-county-kenya-as-of-1-may-2024
dataset_id: rdls_hel-ken_unosat_floodimpactcroplandnairob_20240508
description: "UNOSAT code: FL20240426KEN, GDACS ID: 1102561 This map illustrates satellite-detected\
  \ surface waters in Nairobi and Kiambu County, Kenya, as observed from a Pl\xE9\
  iades image acquired on 1 May 2024 at 11:06 local time (08:06 UTC). Within the analyzed\
  \ area, about 3 km\xB2 of cropland appears to be inundated This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/flood-impact-to-cropland-in-nairobi-and-kiambu-county-kenya-as-of-1-may-2024]"
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
    description: Cropland area in Nairobi and Kiambu County
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AA:km2
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Pl\xE9iades satellite imagery acquired on 1 May 2024 was analyzed\
    \ by UNOSAT analysts using change detection methods comparing pre- and post-flood\
    \ images to identify surface water extent. Inundated cropland area (3 km\xB2)\
    \ was delineated and vectorized into geodatabase and shapefile formats for Nairobi\
    \ and Kiambu County. This is a preliminary post-event damage assessment not yet\
    \ validated in the field."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/flood-impact-to-cropland-in-nairobi-and-kiambu-county-kenya-as-of-1-may-2024
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct cropland inundation from pluvial flooding detected via satellite
      imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood Impact to Cropland in Nairobi and Kiambu County, Kenya as of
    1 May 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3836/FL20240426KEN_gdb.zip
  format: Geodatabase
  id: resource_ea16633a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240426KEN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood Impact to Cropland in Nairobi and Kiambu County, Kenya as of
    1 May 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3836/FL20240426KEN_SHP.zip
  format: null
  id: resource_efd8a580
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240426KEN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ken_unosat_floodimpactcroplandnairob_20240508
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-05-08'
temporal_resolution: null
title: Flood Impact to Cropland in Nairobi and Kiambu County, Kenya as of 1 May 2024
version: null
vulnerability: null
---
