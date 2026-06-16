---
attributions:
- entity:
    affiliation: null
    email: null
    name: VIIRS-NOAA satellite imagery
    url: https://data.humdata.org/dataset/water-extents-as-of-6-november-2019-over-hiraan-middle-shabelle-and-lower-shabelle-region-
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population estimates
    url: https://data.humdata.org/dataset/water-extents-as-of-6-november-2019-over-hiraan-middle-shabelle-and-lower-shabelle-region-
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-as-of-6-november-2019-over-hiraan-middle-shabelle-and-lower-shabelle-region-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-as-of-6-november-2019-over-hiraan-middle-shabelle-and-lower-shabelle-region-
dataset_id: rdls_hel-som_unosat_detectedwaterextentsas6no_20191113
description: 'UNOSAT code: FL20191030SOM This map illustrates the extent of surface
  waters detected over Hiraan, Middle Shabelle and Lower Shabelle Region in Somalia
  as detect by VIIRS-NOAA satellite between 2 & 6 November 2019. In the analysed area,
  a total of about 830 km2 are likely flooded and about 74,000 people might be exposed
  by taking into account WorldPop population estimates. About 10 km of the roads seem
  to be affected. This is a preliminary analysis and has not yet been validated in
  the field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/water-extents-as-of-6-november-2019-over-hiraan-middle-shabelle-and-lower-shabelle-region-]'
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
    description: Residential population exposed to detected flood extent estimated
      at approximately 74,000 people using WorldPop population data
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
- asset_type:
    description: Road network affected by flood extent, approximately 10 km of roads
      impacted
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed VIIRS-NOAA satellite imagery acquired between\
    \ 2-6 November 2019 over Somalia, comparing multi-temporal images to detect surface\
    \ water extent changes and delineate flooded areas. Detected water extent (830\
    \ km\xC2\xB2) was intersected with WorldPop population estimates to quantify exposed\
    \ population (~74,000 people) and overlaid with road networks to assess infrastructure\
    \ impact. This preliminary analysis was not field-validated."
  sources:
  - id: source_1
    license: null
    name: VIIRS-NOAA satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population estimates
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-as-of-6-november-2019-over-hiraan-middle-shabelle-and-lower-shabelle-region-
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to detected flood extent in Hiraan, Middle Shabelle
      and Lower Shabelle regions
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
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Road infrastructure affected by flood extent
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
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
  description: Somalia - Satellite-detected water extents, as of 6 November 2019 over
    Hiraan, Middle Shabelle and Lower Shabelle Region of Somali (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/FL20191030SOM/FL20191030SOM_gdb.zip
  format: Geodatabase
  id: resource_c92dbf49
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191030SOM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Satellite-detected water extents, as of 6 November 2019 over
    Hiraan, Middle Shabelle and Lower Shabelle Region of Somali (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/FL20191030SOM/FL20191030SOM_SHP.zip
  format: null
  id: resource_052f4303
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191030SOM_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-som_unosat_detectedwaterextentsas6no_20191113
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-11-13'
temporal_resolution: null
title: Somalia - Satellite-detected water extents, as of 6 November 2019 over Hiraan,
  Middle Shabelle and Lower Shabelle Region of Somali
version: null
vulnerability: null
---
