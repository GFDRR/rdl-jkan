---
attributions:
- entity:
    affiliation: null
    email: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    url: https://data.humdata.org/dataset/hdx-hapi-fsm
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/hdx-hapi-fsm
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR - The UN Refugee Agency
    url: https://data.humdata.org/dataset/hdx-hapi-fsm
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP - World Food Programme
    url: https://data.humdata.org/dataset/hdx-hapi-fsm
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-fsm
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-fsm
dataset_id: rdls_hel-fsm_hdxapi_hdxhapimicronesiafederate_2002
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-fsm]'
details: HDX HAPI is refreshed daily, but the source datasets may have different update
  schedules. Please refer to the source datasets for each subcategory to verify their
  specific update frequency.
exposure:
- asset_type:
    description: Baseline population by gender and age range at administrative levels
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
      intensity_measure: rainfall:mm
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: drought
license: CC-BY-4.0
lineage:
  description: HDX HAPI aggregates standardized humanitarian indicators from multiple
    authoritative sources (ACLED, INFORM, UNHCR, WFP) through automated data pipelines.
    Rainfall observations are processed to calculate anomalies against long-term averages
    for drought monitoring. Conflict events and displacement populations are compiled
    from source registries and integrated with baseline population data to enable
    interoperable humanitarian decision support.
  sources:
  - id: source_1
    license: null
    name: Armed Conflict Location & Event Data Project (ACLED)
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
    name: UNHCR - The UN Refugee Agency
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: WFP - World Food Programme
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-fsm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Conflict-related fatalities from armed events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: rainfall:mm
      process: null
      trigger: null
      type: drought
    id: loss_1
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
    description: Refugees and persons of concern affected by displacement
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: rainfall:mm
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Refugees and Persons of Concern data from HDX HAPI, please see the
    documentation for more information Source: UNHCR - The UN Refugee Agency License:
    Creative Commons Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/0b87d092-80b5-4a49-bc4e-b754f2eb6ff9/resource/ab72b121-bf75-4146-ac0c-ddd7b9fe79c2/download/hdx_hapi_refugees_fsm.csv
  format: null
  id: resource_ab72b121
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Refugees & Persons of Concern for Micronesia (Federated
    States of)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Conflict Event data from HDX HAPI, please see the documentation for
    more information Source: Armed Conflict Location & Event Data Project (ACLED)
    License: By using ACLED data you agree to abide by the Terms of Use and Attribution
    Policy .'
  download_url: https://data.humdata.org/dataset/0b87d092-80b5-4a49-bc4e-b754f2eb6ff9/resource/b833d13f-fd3b-4e62-bc11-a92097373673/download/hdx_hapi_conflict_event_fsm.csv
  format: null
  id: resource_b833d13f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Conflict Events for Micronesia (Federated States
    of)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'National Risk data from HDX HAPI, please see the documentation for
    more information Source: INFORM License: Creative Commons Attribution International
    (CC BY)'
  download_url: https://data.humdata.org/dataset/0b87d092-80b5-4a49-bc4e-b754f2eb6ff9/resource/1ed2e862-bdfe-455c-8328-12ab0d0632a5/download/hdx_hapi_national_risk_fsm.csv
  format: null
  id: resource_1ed2e862
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: National Risk for Micronesia (Federated States of)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Baseline Population data from HDX HAPI, please see the documentation
    for more information Source: OCHA Office of the Pacific Islands License: Creative
    Commons Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/0b87d092-80b5-4a49-bc4e-b754f2eb6ff9/resource/c0158413-b6bc-4314-b5a1-39b63f50a656/download/hdx_hapi_population_fsm.csv
  format: null
  id: resource_c0158413
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Geography & Infrastructure: Baseline Population for Micronesia (Federated
    States of)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rainfall data from HDX HAPI, please see the documentation for more
    information Source: WFP - World Food Programme License: Creative Commons Attribution
    International (CC BY)'
  download_url: https://data.humdata.org/dataset/0b87d092-80b5-4a49-bc4e-b754f2eb6ff9/resource/120818fa-6330-494c-b08e-ddf4255c87e4/download/hdx_hapi_rainfall_fsm.csv
  format: null
  id: resource_120818fa
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Climate: Rainfall for Micronesia (Federated States of)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Data Availability Data from HDX HAPI. Each row in this resource represents
    an administrative division for which data is available, by subcategory. Please
    see the documentation for more information Source: HDX HAPI License: Creative
    Commons Attribution for Intergovernmental Organisations'
  download_url: https://data.humdata.org/dataset/0b87d092-80b5-4a49-bc4e-b754f2eb6ff9/resource/17deee7f-ad18-4e9b-b7a3-f201df0cd46d/download/hdx_hapi_data_availability_fsm.csv
  format: null
  id: resource_17deee7f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Metadata: Data Availability for Micronesia (Federated States of)'
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-fsm_hdxapi_hdxhapimicronesiafederate_2002
spatial:
  bbox: null
  centroid: null
  countries:
  - FSM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-31'
  start: '2002-01-01'
temporal_resolution: null
title: HDX HAPI Data for Micronesia (Federated States of)
version: null
vulnerability: null
---
