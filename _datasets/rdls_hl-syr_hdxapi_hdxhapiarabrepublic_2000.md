---
attributions:
- entity:
    affiliation: null
    email: null
    name: ACLED (Armed Conflict Location & Event Data Project)
    url: https://data.humdata.org/dataset/hdx-hapi-syr
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/hdx-hapi-syr
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM (International Organization for Migration)
    url: https://data.humdata.org/dataset/hdx-hapi-syr
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA FTS (Financial Tracking System)
    url: https://data.humdata.org/dataset/hdx-hapi-syr
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA HPC Tools (Humanitarian Programme Cycle)
    url: https://data.humdata.org/dataset/hdx-hapi-syr
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR (The UN Refugee Agency)
    url: https://data.humdata.org/dataset/hdx-hapi-syr
  id: attribution_6
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP (World Food Programme)
    url: https://data.humdata.org/dataset/hdx-hapi-syr
  id: attribution_7
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-syr
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-syr
dataset_id: rdls_hl-syr_hdxapi_hdxhapiarabrepublic_2000
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-syr]'
details: HDX HAPI is refreshed daily, but the source datasets may have different update
  schedules. Please refer to the source datasets for each subcategory to verify their
  specific update frequency.
exposure: []
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
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: HDX HAPI aggregates standardized humanitarian indicators from multiple
    UN agencies and international organizations (ACLED, IOM, UNHCR, WFP, OCHA) into
    a unified API for Syrian Arab Republic. Rainfall observations and national risk
    assessments provide hazard context, while displacement, refugee, returnee, and
    humanitarian needs data from partner organizations are compiled into consistent
    administrative and temporal structures to support humanitarian decision-making
    workflows.
  sources:
  - id: source_1
    license: null
    name: ACLED (Armed Conflict Location & Event Data Project)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: INFORM
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: IOM (International Organization for Migration)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: OCHA FTS (Financial Tracking System)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: OCHA HPC Tools (Humanitarian Programme Cycle)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_6
    license: null
    name: UNHCR (The UN Refugee Agency)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_7
    license: null
    name: WFP (World Food Programme)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-syr
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons affected by humanitarian crisis in Syrian
      Arab Republic
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Refugees and persons of concern from Syrian Arab Republic
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Returnees to Syrian Arab Republic
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population with humanitarian needs in Syrian Arab Republic
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "IDPs data from HDX HAPI, please see the documentation for more information\
    \ Source: International Organization for Migration (IOM) License: Copyright \xC2\
    \xA9 International Organization for Migration 2018 IOM reserves the right to assert\
    \ ownership of the Materials collected on the https://data.humdata.org/ website.\
    \ The Materials may be viewed, downloaded, and printed for non-commercial use\
    \ only, without, inter alia, any right to sell, resell, redistribute or create\
    \ derivative works therefrom. At all times the User shall credit the DTM as the\
    \ source, unless otherwise stated. The user must include the URL of the Materials\
    \ from the HDX Website, as well as the following credit line: Source: 'International\
    \ Organization for Migration (IOM), Displacement Tracking Matrix (DTM)'."
  download_url: https://data.humdata.org/dataset/a8b2f1dc-6428-4e86-b147-55a12d9de481/resource/92cb0239-b8d4-4a70-bd4a-9a71364543a0/download/hdx_hapi_idps_syr.csv
  format: null
  id: resource_92cb0239
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Internally-Displaced Persons for Syrian Arab Republic'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Refugees and Persons of Concern data from HDX HAPI, please see the
    documentation for more information Source: UNHCR - The UN Refugee Agency License:
    Creative Commons Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/a8b2f1dc-6428-4e86-b147-55a12d9de481/resource/80b39481-c161-4655-b2e4-677c1b259fab/download/hdx_hapi_refugees_syr.csv
  format: null
  id: resource_80b39481
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Refugees & Persons of Concern for Syrian Arab Republic'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Returnees data from HDX HAPI, please see the documentation for more
    information Source: UNHCR - The UN Refugee Agency License: Creative Commons Attribution
    for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/a8b2f1dc-6428-4e86-b147-55a12d9de481/resource/9745fb4c-b48a-4fbf-bc00-dda577ebb488/download/hdx_hapi_returnees_syr.csv
  format: null
  id: resource_9745fb4c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Returnees for Syrian Arab Republic'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Humanitarian needs data from HDX HAPI, please see the documentation
    for more information Source: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
    License: Creative Commons Attribution for Intergovernmental Organisations (CC
    BY-IGO)'
  download_url: https://data.humdata.org/dataset/a8b2f1dc-6428-4e86-b147-55a12d9de481/resource/a40a1e89-b40d-4b00-845b-fc2bf9d9cc94/download/hdx_hapi_humanitarian_needs_syr.csv
  format: null
  id: resource_a40a1e89
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Humanitarian Needs for Syrian Arab Republic'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Funding data from HDX HAPI, please see the documentation for more
    information Source: OCHA Financial Tracking System (FTS) License: Creative Commons
    Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/a8b2f1dc-6428-4e86-b147-55a12d9de481/resource/aad3e15e-b890-4d6b-878a-535837686d15/download/hdx_hapi_funding_syr.csv
  format: null
  id: resource_aad3e15e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Funding for Syrian Arab Republic'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Conflict Event data from HDX HAPI, please see the documentation for
    more information Source: Armed Conflict Location & Event Data Project (ACLED)
    License: By using ACLED data you agree to abide by the Terms of Use and Attribution
    Policy .'
  download_url: https://data.humdata.org/dataset/a8b2f1dc-6428-4e86-b147-55a12d9de481/resource/6b3efb18-ec78-4f91-85ba-d992fc9ac363/download/hdx_hapi_conflict_event_syr.csv
  format: null
  id: resource_6b3efb18
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Conflict Events for Syrian Arab Republic'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'National Risk data from HDX HAPI, please see the documentation for
    more information Source: INFORM License: Creative Commons Attribution International
    (CC BY)'
  download_url: https://data.humdata.org/dataset/a8b2f1dc-6428-4e86-b147-55a12d9de481/resource/976fb8d9-a3ec-4af9-af6c-348cea66003e/download/hdx_hapi_national_risk_syr.csv
  format: null
  id: resource_976fb8d9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: National Risk for Syrian Arab Republic'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Food Prices & Market Monitor data from HDX HAPI, please see the documentation
    for more information Source: WFP - World Food Programme License: Creative Commons
    Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/a8b2f1dc-6428-4e86-b147-55a12d9de481/resource/e6e2abd1-3876-48ff-817b-ba7fc516991f/download/hdx_hapi_food_price_syr.csv
  format: null
  id: resource_e6e2abd1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Food Prices & Market Monitor for Syrian
    Arab Republic'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rainfall data from HDX HAPI, please see the documentation for more
    information Source: WFP - World Food Programme License: Creative Commons Attribution
    International (CC BY)'
  download_url: https://data.humdata.org/dataset/a8b2f1dc-6428-4e86-b147-55a12d9de481/resource/a7445150-96bb-4752-baad-7536ecd8fd84/download/hdx_hapi_rainfall_syr.csv
  format: null
  id: resource_a7445150
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Climate: Rainfall for Syrian Arab Republic'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Data Availability Data from HDX HAPI. Each row in this resource represents
    an administrative division for which data is available, by subcategory. Please
    see the documentation for more information Source: HDX HAPI License: Creative
    Commons Attribution for Intergovernmental Organisations'
  download_url: https://data.humdata.org/dataset/a8b2f1dc-6428-4e86-b147-55a12d9de481/resource/b9820645-0cc8-4568-a9cc-ef269ce62bfe/download/hdx_hapi_data_availability_syr.csv
  format: null
  id: resource_b9820645
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Metadata: Data Availability for Syrian Arab Republic'
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-syr_hdxapi_hdxhapiarabrepublic_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2028-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: HDX HAPI Data for Syrian Arab Republic
version: null
vulnerability: null
---
