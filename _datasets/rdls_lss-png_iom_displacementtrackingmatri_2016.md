---
attributions:
- entity:
    affiliation: null
    email: null
    name: IOM Displacement Tracking Matrix (DTM) API
    url: https://data.humdata.org/dataset/png-iom-dtm-from-api
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/png-iom-dtm-from-api
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/png-iom-dtm-from-api
dataset_id: rdls_lss-png_iom_displacementtrackingmatri_2016
description: 'This dataset comes from the International Organization for Migration
  (IOM)''s displacement tracking matrix (DTM) publicly accessible API . This API allows
  the humanitarian community, academia, media, government, and non-governmental organizations
  to utilize the data collected by DTM. The DTM API only provides non-sensitive IDP
  figures, aggregated at the country, Admin 1 (states, provinces, or equivalent),
  and Admin 2 (smaller subnational administrative areas) levels. For more detailed
  information, please see the country-specific DTM datasets on HDX .. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/png-iom-dtm-from-api]'
details: This dataset comes from the [DTM API](https://dtm.iom.int/data-and-analysis/dtm-api),
  which provides only non-sensitive IDP figures, aggregated at the country, Admin
  1, and Admin 2 levels. For more detailed information, please see the [country-specific
  DTM datasets on HDX](https://data.humdata.org/dataset/?dataseries_name=IOM%20-%20DTM%20Baseline%20Assessment&dataseries_name=IOM%20-%20DTM%20Event%20and%20Flow%20Tracking&dataseries_name=IOM%20-%20DTM%20Site%20and%20Location%20Assessment&organization=international-organization-for-migration&q=&sort=last_modified%20desc&ext_page_size=25).
  IOM is continually adding new data as well as updating data that's already been
  added.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: "Displacement figures are collected by IOM field teams in Papua New\
    \ Guinea using the DTM methodological framework, encompassing baseline assessments\
    \ (BA), emergency tracking tools (ETT), and site assessments (SA). Data are aggregated\
    \ at admin levels 0\xE2\u20AC\u201C2 and served via the DTM public API, providing\
    \ temporally stamped IDP counts disaggregated by displacement reason, sex, and\
    \ origin area for humanitarian monitoring and response planning."
  sources:
  - id: source_1
    license: null
    name: IOM Displacement Tracking Matrix (DTM) API
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/png-iom-dtm-from-api
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: IDP counts aggregated at admin 0-2 levels with displacement reason
      including conflict and natural hazards, tracked via IOM DTM baseline and emergency
      assessments
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
  url: https://dtm.iom.int/about/methodological-framework
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Papua New Guinea IOM displacement tracking matrix data at admin levels
    0-2, sourced from the DTM API
  download_url: https://data.humdata.org/dataset/0027fa21-c67d-45f1-8b97-ec084d6ea23d/resource/c51fbea2-b9d0-4609-bc56-2dbec7cc7e39/download/png-iom-dtm-from-api-admin-0-to-2.csv
  format: null
  id: resource_c51fbea2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Papua New Guinea IOM DTM data for admin levels 0-2
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-png_iom_displacementtrackingmatri_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - PNG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-07-30'
  start: '2016-10-01'
temporal_resolution: null
title: Papua New Guinea IOM Displacement Tracking Matrix (DTM) from API
version: null
vulnerability: null
---
