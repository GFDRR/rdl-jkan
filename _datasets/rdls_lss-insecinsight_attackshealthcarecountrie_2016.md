---
attributions:
- entity:
    affiliation: null
    email: null
    name: Safeguarding Health in Conflict Coalition (SHCC)
    url: https://data.humdata.org/dataset/shcchealthcare-dataset
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Insecurity Insight
  url: https://data.humdata.org/dataset/shcchealthcare-dataset
creator:
  affiliation: null
  email: null
  name: Insecurity Insight
  url: https://data.humdata.org/dataset/shcchealthcare-dataset
dataset_id: rdls_lss-insecinsight_attackshealthcarecountrie_2016
description: 'This dataset contains agency- and open source events published in the
  Attacks on Health Care News Brief and included in the Safeguarding Health in Conflict
  Coalition (SHCC) annual reporting on violence against or obstruction of health care.
  This page is managed by SHCC member Insecurity Insight. Please get in touch if you
  are interested in curated datasets: info@insecurityinsight.org. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/shcchealthcare-dataset]'
details: Not representative or a comprehensive compilation of all events in which
  health care was affected. Where the number of health workers, facilities or ambulances
  affected is unspecified, one is counted.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Incident-level data compiled from agency reports and open source monitoring
    of attacks on healthcare facilities and workers in conflict settings. Events are
    geocoded and categorized by attack type, perpetrator, and impact metrics including
    facility damage, health worker casualties, and obstruction of care.
  sources:
  - id: source_1
    license: null
    name: Safeguarding Health in Conflict Coalition (SHCC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Insecurity Insight
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/shcchealthcare-dataset
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Health facility destruction and damage from conflict-related attacks
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Health workers killed in attacks on healthcare
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Health workers injured in attacks on healthcare
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: ppl_injured
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
  url: http://insecurityinsight.org/methodology-and-definitions#section_attacks_on_health_care
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains all incidents of violence against or obstruction of
    access to health care between in 2024 identified by the Safeguarding Health in
    Conflict Coalition (SHCC) and cited in the report Epidemic of Vioelnce .
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/f86f3f9b-1e82-491a-a3eb-7fd59e7020f4/download/2024-shcc-incident-data.xlsx
  format: null
  id: resource_f86f3f9b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2024 SHCC Incident Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains reported incidents of violence against or obstruction
    of healthcare in 2024 identified by the Safeguarding Health in Conflict Coalition
    (SHCC) and cited in the report Epidemic of Violence . Read the factsheet
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/f28d2a58-bab5-4207-9251-87fa11d9c62c/download/2023-2024-ind-shcc-health-care-data.xlsx
  format: null
  id: resource_f28d2a58
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2023-2024 IND SHCC Health Care Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains reported incidents of violence against or obstruction
    of healthcare in 2024 identified by the Safeguarding Health in Conflict Coalition
    (SHCC) and cited in the report Epidemic of Violence . Read the factsheet
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/6e32b128-b65c-49ea-b535-1f9171ec7ce9/download/2022-2024-col-shcc-health-care-data.xlsx
  format: null
  id: resource_6e32b128
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2022-2024 COL SHCC Health Care Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains all incidents of violence against or obstruction of
    access to health care between in 2023 identified by the Safeguarding Health in
    Conflict Coalition (SHCC) and cited in the report Critical Conditions .
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/9ce3ac0a-7626-40d6-a2ff-65b957101fd0/download/2023-shcc-incident-data.xlsx
  format: null
  id: resource_9ce3ac0a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2023 SHCC Incident Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains reported incidents of violence against or obstruction
    of healthcare in India (Manipur state only) in 2023 identified by the Safeguarding
    Health in Conflict Coalition (SHCC) and cited in the report Critical Conditions
    . Read the factsheet
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/cda35084-bd6c-4ae9-998f-96009e514129/download/2023-ind-shcc-health-care-data.xlsx
  format: null
  id: resource_cda35084
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2023 IND SHCC Health Care Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains reported incidents of violence against or obstruction
    of healthcare in Israel in 2023 identified by the Safeguarding Health in Conflict
    Coalition (SHCC) and cited in the report Critical Conditions . Read the factsheet
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/39f0b2f1-0a17-45b1-9c51-fc1da2308a30/download/2023-isr-shcc-health-care-data.xlsx
  format: null
  id: resource_39f0b2f1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2023 ISR SHCC Health Care Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains all incidents of violence against or obstruction of
    access to health care between 1st January and 31st December 2022 as documented
    in the 2022 Safeguarding Health in Conflict Coalition Report.
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/7106abfe-384a-4e26-86ab-eed828e91d63/download/2022-shcc-incident-data.xlsx
  format: null
  id: resource_7106abfe
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2022 SHCC Incident Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset contains the total number of incidents reported per country
    in 2021.
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/bb208555-c7dd-4374-a0bb-d17ee8281d3f/download/2021-shcc-overview-data.xlsx
  format: null
  id: resource_bb208555
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2021 SHCC Overview Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'January-December 2021: This dataset contains only events that are
    perpetrated by conflict actors, defined as state security forces or non-state
    actors engaged in armed conflict or who carry out one-sided violence against civilians.
    It provides details on the perpetrator and the weapon use. This dataset follows
    the definition and methodology of the Safeguarding Health in Conflict Coalition
    (SHCC). See https://bit.ly/3daW5uJ for definitions and methodology. Read the report
    that accompanies this dataset:'
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/93bc317a-189b-4b91-9564-c8334ab687c9/download/2021-shcc-incident-data.xlsx
  format: null
  id: resource_93bc317a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2021 SHCC Incident Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'January-December 2020: This dataset contains only events that are
    perpetrated by conflict actors, defined as state security forces or non-state
    actors engaged in armed conflict or who carry out one-sided violence against civilians.
    It provides details on the perpetrator and the weapon use. This dataset follows
    the definition and methodology of the Safeguarding Health in Conflict Coalition
    (SHCC). See https://bit.ly/3daW5uJ for methodology. Read the report that accompanies
    this dataset: https://bit.ly/2DvqoQg'
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/a4ba203d-5e5b-477b-9524-784a544be094/download/2020-shcc-incident-data.xlsx
  format: null
  id: resource_a4ba203d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2020 SHCC Incident Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset contains the total number of incidents reported per country
    in 2020.
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/07f5eefa-cf0d-4dd5-88db-c6a9a3fc26be/download/2020-shcc-overview-data.xlsx
  format: null
  id: resource_07f5eefa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2020 SHCC Overview Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset contains global incidents of violence against or obstruction
    of health care between 2016 and 2020.
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/b23b91e2-9146-4275-899f-6db47b22fedb/download/five-year-review-violence-against-or-obstruction-of-health-care-2016-2020-data.xlsx
  format: null
  id: resource_b23b91e2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Five-year review Violence Against or Obstruction of Health Care 2016-2020
    Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Attacks on Health Care in Countries in Conflict (SHCC) Data (This dataset
    contains each reported incident in 2019.)
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/0ddd9b34-7599-4a9a-af36-acb3b37c75a7/download/2019-shcc-incident-data.xlsx
  format: null
  id: resource_0ddd9b34
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2019 SHCC Incident Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Attacks on Health Care in Countries in Conflict (SHCC) Data (This dataset
    contains the total number of attacks reported per country in 2019.)
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/5a553515-f528-469d-9db5-2c50985e6cfd/download/2019-shcc-overview-data.xlsx
  format: null
  id: resource_5a553515
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2019 SHCC Overview Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Attacks on Health Care in Countries in Conflict (SHCC) Data (This dataset
    contains the total number of attacks reported per country in 2018.)
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/d053b42a-7d31-41b5-a6d9-c8b0a424241c/download/2018-shcc-overview-data.xlsx
  format: null
  id: resource_d053b42a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2018 SHCC Overview Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Attacks on Health Care in Countries in Conflict (SHCC) Data (This dataset
    contains each reported attack in 2018.)
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/53dccce9-51c1-4125-bc9b-bef7604c106b/download/2018-shcc-attacks-data.xlsx
  format: null
  id: resource_53dccce9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2018 SHCC Attacks Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Attacks on Health Care in Countries in Conflict (SHCC) Data (This dataset
    contains the total number of attacks reported per country in 2017.)
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/cf235bb7-33d1-4770-af50-d906c2234b91/download/2017-shcc-overview-data.xlsx
  format: null
  id: resource_cf235bb7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2017 SHCC Overview Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains reported incidents of violence against or obstruction
    of healthcare in 2024 identified by the Safeguarding Health in Conflict Coalition
    (SHCC) and cited in the report Epidemic of Violence . Read the factsheet
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/bce8a63c-38ef-4934-9a94-fc4968f1e7d2/download/2022-2024-col-shcc-health-care-data.xlsx
  format: null
  id: resource_bce8a63c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2022-2024 COL SHCC Health Care Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains reported incidents of violence against or obstruction
    of healthcare in 2024 identified by the Safeguarding Health in Conflict Coalition
    (SHCC) and cited in the report Epidemic of Violence . Read the factsheet
  download_url: https://data.humdata.org/dataset/02995168-3644-4b78-92be-cdf67275b39d/resource/d95e5d02-49a2-454d-81cf-f4c2eebcc230/download/2023-2024-ind-shcc-health-care-data.xlsx
  format: null
  id: resource_d95e5d02
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2023-2024 IND SHCC Health Care Data.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-insecinsight_attackshealthcarecountrie_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  - IRQ
  - MKD
  - PSE
  - SYR
  - USA
  - VEN
  - YEM
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2016-01-01'
temporal_resolution: null
title: Attacks on Health Care in Countries in Conflict (SHCC) Data
version: null
vulnerability: null
---
