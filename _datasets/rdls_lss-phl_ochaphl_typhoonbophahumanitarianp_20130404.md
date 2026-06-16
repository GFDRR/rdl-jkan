---
attributions:
- entity:
    affiliation: null
    email: null
    name: Department of Social Welfare and Development (DSWD)
    url: https://data.humdata.org/dataset/philippines-other-0-0-0-0-0-0-0-0-0-0-0-0
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Disaster Response Operations Monitoring and Information Center (DROMIC)
    url: https://data.humdata.org/dataset/philippines-other-0-0-0-0-0-0-0-0-0-0-0-0
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-other-0-0-0-0-0-0-0-0-0-0-0-0
creator:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-other-0-0-0-0-0-0-0-0-0-0-0-0
dataset_id: rdls_lss-phl_ochaphl_typhoonbophahumanitarianp_20130404
description: 'The dataset shows the Typhoon Bopha Humanitarian Profile as of 05 April
  2013. It contains information on the affected population inside and outside evacuation
  centers by Typhoon Bopha. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/philippines-other-0-0-0-0-0-0-0-0-0-0-0-0]'
details: '**Languages:** EN'
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Data was compiled by DROMIC under DSWD through field-level reporting
    of affected population counts inside and outside evacuation centers following
    Typhoon Bopha (Pablo). The humanitarian profile aggregates displacement and shelter
    impact figures as of 05 April 2013, providing a snapshot of population-level impacts
    for humanitarian coordination purposes.
  sources:
  - id: source_1
    license: null
    name: Department of Social Welfare and Development (DSWD)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Disaster Response Operations Monitoring and Information Center (DROMIC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-other-0-0-0-0-0-0-0-0-0-0-0-0
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Affected population inside and outside evacuation centers following
      Typhoon Bopha in the Philippines as of April 2013
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  description: Philippines - Typhoon Bopha Humanitarian Profile as of 05 April 2013
    (Excel)
  download_url: https://data.humdata.org/dataset/03f5f59e-42a7-4650-8a5a-788e7726ba6c/resource/0029f807-ab75-4fa9-b2bd-ea50f9c72190/download/dromic_report_as_of_05april2013.xls
  format: null
  id: resource_0029f807
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dromic_report_as_of_05april2013.xls
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_ochaphl_typhoonbophahumanitarianp_20130404
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2013-04-04'
temporal_resolution: null
title: Philippines - Typhoon Bopha Humanitarian Profile as of 05 April 2013
version: null
vulnerability: null
---
