---
attributions:
- entity:
    affiliation: null
    email: null
    name: VIIRS-NOAA satellite imagery
    url: https://data.humdata.org/dataset/water-extents-as-of-25-august-2019-over-white-nile-sennar-and-el-gazira-states-in-sudan
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population estimates
    url: https://data.humdata.org/dataset/water-extents-as-of-25-august-2019-over-white-nile-sennar-and-el-gazira-states-in-sudan
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-as-of-25-august-2019-over-white-nile-sennar-and-el-gazira-states-in-sudan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-as-of-25-august-2019-over-white-nile-sennar-and-el-gazira-states-in-sudan
dataset_id: rdls_hel-sdn_unosat_detectedwaterextentsas25a_20190828
description: 'UNOSAT code: FL20190815SDN This map illustrates the extent of surface
  waters detected over El Gazira, White Nile and Sennar states located in the southern
  part of Sudan as detected by VIIRS-NOAA satellite between 22 & 25 August 2019. In
  the analysed area, a total of about 7000 km2 are likely flooded and about 250,000
  people might be affected by taking into account the WorldPop population estimates.
  This is a preliminary analysis that has not yet been validated in the field. Please
  send any field-based comments to UNITAR-UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/water-extents-as-of-25-august-2019-over-white-nile-sennar-and-el-gazira-states-in-sudan]'
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
    description: Residential population estimated from WorldPop data in flood-affected
      areas
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts compared VIIRS-NOAA satellite imagery acquired between\
    \ 22-25 August 2019 to detect surface water extent changes over El Gazira, White\
    \ Nile, and Sennar states. Detected water bodies were mapped as polygons with\
    \ area calculations (7000 km\xC2\xB2 total). WorldPop population estimates were\
    \ overlaid to estimate approximately 250,000 affected people. This is a preliminary\
    \ post-event assessment not yet validated in the field."
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
- href: https://data.humdata.org/dataset/water-extents-as-of-25-august-2019-over-white-nile-sennar-and-el-gazira-states-in-sudan
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by detected flood extent based on WorldPop estimates
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
  description: Satellite detected water extents, as of 25 August 2019 over White Nile,
    Sennar and El Gazira states in Sudan (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20190815SDN/FL20190815SDN_gdb.zip
  format: Geodatabase
  id: resource_63b615c4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20190815SDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents, as of 25 August 2019 over White Nile,
    Sennar and El Gazira states in Sudan (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20190815SDN/FL20190815SDN_SHP.zip
  format: null
  id: resource_05606005
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20190815SDN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-sdn_unosat_detectedwaterextentsas25a_20190828
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-08-28'
temporal_resolution: null
title: Satellite detected water extents, as of 25 August 2019 over White Nile, Sennar
  and El Gazira states in Sudan
version: null
vulnerability: null
---
