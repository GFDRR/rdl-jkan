---
attributions:
- entity:
    affiliation: null
    email: null
    name: Internal Displacement Monitoring Centre (IDMC)
    url: https://data.humdata.org/dataset/iom-global-profiles-for-internal-displacement-gpid
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/iom-global-profiles-for-internal-displacement-gpid
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/iom-global-profiles-for-internal-displacement-gpid
dataset_id: rdls_lss-iom_globalprofilesinternaldis_2018
description: 'While the total numbers of internal displacements - by cause, location,
  and time - are well documented, global estimates of the demographic and socio-economic
  profiles of impacted communities have been largely missing. This lack of disaggregated
  data on variables such as age, sex, income, education, health, and land use, has
  limited understanding of the diverse vulnerabilities and needs of displacement-affected
  populations - complicating the work of decision makers tasked with allocating resources
  effectively. The Global Profiles for Internal Displacement (GPID) dataset aims to
  bridge this gap. By combining geolocated displacement data from the Internal Displacement
  Monitoring Centre (IDMC) with high-resolution global maps of demographic and socio-economic
  indicators, the dataset provides consistent estimates of key characteristics of
  populations in locations impacted by internal displacement - annually since 2018
  at global, regional, and national level. Find out more on the GPID website .. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/iom-global-profiles-for-internal-displacement-gpid]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: GPID aggregates internal displacement data from IDMC across multiple
    hazard causes (flood, drought, earthquake, cyclones, conflict) and enriches it
    with disaggregated demographic variables (age, sex, income, education, health,
    land use) to create population profiles at global, regional, and country levels.
    The dataset bridges the gap between total displacement counts and detailed vulnerability
    characterization of displacement-affected communities.
  sources:
  - id: source_1
    license: null
    name: Internal Displacement Monitoring Centre (IDMC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/iom-global-profiles-for-internal-displacement-gpid
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced populations from flooding with demographic and
      socio-economic profiles
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced populations from drought with demographic and
      socio-economic profiles
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced populations from earthquakes with demographic
      and socio-economic profiles
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced populations from cyclones/hurricanes with demographic
      and socio-economic profiles
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://dtm.iom.int/global-profiles-for-internal-displacement/gpid/index.html
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IOM - Global Profiles for Internal Displacement (GPID) (GPID v1.0 -
    Readme)
  download_url: https://data.humdata.org/dataset/71a5658e-d896-4d64-a8ff-a0b2b9441dcb/resource/34546f8f-8006-430a-a871-39faa1e97157/download/gpid-v1.0-readme.txt
  format: null
  id: resource_34546f8f
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GPID v1.0 - Readme
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file provides demographic, socio-economic, and land use profiles
    of populations in areas that experienced internal displacement due to conflict
    and different disaster types during 2018-2024, at global level.
  download_url: https://data.humdata.org/dataset/71a5658e-d896-4d64-a8ff-a0b2b9441dcb/resource/0c5a6e77-dbeb-4c0d-a51f-22f8aca3eece/download/gpid-v1.0-global-level.csv
  format: null
  id: resource_0c5a6e77
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GPID v1.0 - Global level
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file provides demographic, socio-economic, and land use profiles
    of populations in areas that experienced internal displacement due to conflict
    and different disaster types during 2018-2024, at regional level.
  download_url: https://data.humdata.org/dataset/71a5658e-d896-4d64-a8ff-a0b2b9441dcb/resource/d3d344ff-fc43-439d-accf-50afc391137a/download/gpid-v1.0-regional-level.csv
  format: null
  id: resource_d3d344ff
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GPID v1.0 - Regional level
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file provides demographic, socio-economic, and land use profiles
    of populations in areas that experienced internal displacement due to conflict
    and different disaster types during 2018-2024, at country level.
  download_url: https://data.humdata.org/dataset/71a5658e-d896-4d64-a8ff-a0b2b9441dcb/resource/a435a32e-9827-4016-b568-7c3425cff8c1/download/gpid-v1.0-country-level.csv
  format: null
  id: resource_a435a32e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GPID v1.0 - Country level
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-iom_globalprofilesinternaldis_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2018-01-01'
temporal_resolution: null
title: IOM - Global Profiles for Internal Displacement (GPID)
version: null
vulnerability: null
---
