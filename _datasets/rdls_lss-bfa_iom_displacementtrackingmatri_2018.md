---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/bfa-iom-dtm-from-api
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/bfa-iom-dtm-from-api
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/bfa-iom-dtm-from-api
dataset_id: rdls_lss-bfa_iom_displacementtrackingmatri_2018
description: 'This dataset comes from the International Organization for Migration
  (IOM)''s displacement tracking matrix (DTM) publicly accessible API . This API allows
  the humanitarian community, academia, media, government, and non-governmental organizations
  to utilize the data collected by DTM. The DTM API only provides non-sensitive IDP
  figures, aggregated at the country, Admin 1 (states, provinces, or equivalent),
  and Admin 2 (smaller subnational administrative areas) levels. For more detailed
  information, please see the country-specific DTM datasets on HDX .. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/bfa-iom-dtm-from-api]'
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
  description: IOM DTM field teams conduct baseline assessments, emergency tracking,
    and site assessments to enumerate internally displaced populations across Burkina
    Faso. Data is aggregated at admin 0, 1, and 2 levels and published through the
    DTM API, with displacement counts disaggregated by sex and reason for displacement.
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
- href: https://data.humdata.org/dataset/bfa-iom-dtm-from-api
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons counts disaggregated by sex and displacement
      reason from conflict-related displacement
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
  description: Burkina Faso IOM displacement tracking matrix data at admin levels
    0-2, sourced from the DTM API
  download_url: https://data.humdata.org/dataset/93913ac7-7a78-4967-99fb-e9f071756971/resource/c775ef63-4cd0-4bb6-80cc-a28245b9fe60/download/bfa-iom-dtm-from-api-admin-0-to-2.csv
  format: null
  id: resource_c775ef63
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Burkina Faso IOM DTM data for admin levels 0-2
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bfa_iom_displacementtrackingmatri_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - BFA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-08-30'
  start: '2018-10-30'
temporal_resolution: null
title: Burkina Faso IOM Displacement Tracking Matrix (DTM) from API
version: null
vulnerability: null
---
