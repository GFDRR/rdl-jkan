---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/vct-iom-dtm-from-api
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/vct-iom-dtm-from-api
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/vct-iom-dtm-from-api
dataset_id: rdls_lss-vct_iom_saintvincentgrenadinesdis_20240731
description: 'This dataset comes from the International Organization for Migration
  (IOM)''s displacement tracking matrix (DTM) publicly accessible API . This API allows
  the humanitarian community, academia, media, government, and non-governmental organizations
  to utilize the data collected by DTM. The DTM API only provides non-sensitive IDP
  figures, aggregated at the country, Admin 1 (states, provinces, or equivalent),
  and Admin 2 (smaller subnational administrative areas) levels. For more detailed
  information, please see the country-specific DTM datasets on HDX .. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/vct-iom-dtm-from-api]'
details: This dataset comes from the [DTM API](https://dtm.iom.int/data-and-analysis/dtm-api),
  which provides only non-sensitive IDP figures, aggregated at the country, Admin
  1, and Admin 2 levels. For more detailed information, please see the [country-specific
  DTM datasets on HDX](https://data.humdata.org/dataset/?dataseries_name=IOM%20-%20DTM%20Baseline%20Assessment&dataseries_name=IOM%20-%20DTM%20Event%20and%20Flow%20Tracking&dataseries_name=IOM%20-%20DTM%20Site%20and%20Location%20Assessment&organization=international-organization-for-migration&q=&sort=last_modified%20desc&ext_page_size=25).
  IOM is continually adding new data as well as updating data that's already been
  added.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IDP data collected through IOM's DTM assessment framework (baseline,
    emergency tracking, and site assessments) and aggregated via the publicly accessible
    DTM API at country and Admin 1-2 levels, providing displacement counts disaggregated
    by sex, displacement reason, and origin location.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/vct-iom-dtm-from-api
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons tracked by IOM DTM across administrative
      levels
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
  description: Saint Vincent and the Grenadines IOM displacement tracking matrix data
    at admin levels 0-1, sourced from the DTM API
  download_url: https://data.humdata.org/dataset/4acbee22-ddeb-4262-97ff-b12513436eeb/resource/bbfa382d-3303-467c-b2a3-ca14577aeee4/download/vct-iom-dtm-from-api-admin-0-to-1.csv
  format: null
  id: resource_bbfa382d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Saint Vincent and the Grenadines IOM DTM data for admin levels 0-1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-vct_iom_saintvincentgrenadinesdis_20240731
spatial:
  bbox: null
  centroid: null
  countries:
  - VCT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-07-31'
temporal_resolution: null
title: Saint Vincent and the Grenadines IOM Displacement Tracking Matrix (DTM) from
  API
version: null
vulnerability: null
---
