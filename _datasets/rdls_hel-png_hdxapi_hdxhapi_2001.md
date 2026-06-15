---
attributions:
- entity:
    affiliation: null
    email: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    url: https://data.humdata.org/dataset/hdx-hapi-png
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/hdx-hapi-png
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM)
    url: https://data.humdata.org/dataset/hdx-hapi-png
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Field Information Services Section (FISS)
    url: https://data.humdata.org/dataset/hdx-hapi-png
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Oxford Poverty & Human Development Initiative
    url: https://data.humdata.org/dataset/hdx-hapi-png
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR - The UN Refugee Agency
    url: https://data.humdata.org/dataset/hdx-hapi-png
  id: attribution_6
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP - World Food Programme
    url: https://data.humdata.org/dataset/hdx-hapi-png
  id: attribution_7
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-png
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-png
dataset_id: rdls_hel-png_hdxapi_hdxhapi_2001
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-png]'
details: HDX HAPI is refreshed daily, but the source datasets may have different update
  schedules. Please refer to the source datasets for each subcategory to verify their
  specific update frequency.
exposure:
- asset_type:
    description: Baseline population distribution across administrative divisions
      in Papua New Guinea
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
  event_sets_by_hazard_type:
    drought:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: rfh:mm
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: HDX HAPI aggregates standardized humanitarian indicators from multiple
    UN agencies and research organizations including ACLED, INFORM, IOM, OCHA, UNHCR,
    and WFP. Data is collected through field assessments, administrative registries,
    and conflict event monitoring, then harmonized into common administrative geographies
    and temporal reporting periods to enable interoperable humanitarian decision-making
    workflows.
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
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: OCHA Field Information Services Section (FISS)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: Oxford Poverty & Human Development Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_6
    license: null
    name: UNHCR - The UN Refugee Agency
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_7
    license: null
    name: WFP - World Food Programme
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-png
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Fatalities from conflict events in Papua New Guinea
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: rfh:mm
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
    description: Internally displaced persons from conflict in Papua New Guinea
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: rfh:mm
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
    description: Population affected by poverty and food insecurity in Papua New Guinea
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: rfh:mm
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
        type: indirect
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
  download_url: https://data.humdata.org/dataset/72a8f7aa-14f9-4eb6-a6aa-011d944595f0/resource/c6801624-91c7-4720-a0d6-2cabb1506e74/download/hdx_hapi_idps_png.csv
  format: null
  id: resource_c6801624
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Internally-Displaced Persons for Papua New Guinea'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Refugees and Persons of Concern data from HDX HAPI, please see the
    documentation for more information Source: UNHCR - The UN Refugee Agency License:
    Creative Commons Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/72a8f7aa-14f9-4eb6-a6aa-011d944595f0/resource/e517cfe7-28bb-41ee-9b65-9d8d772596e3/download/hdx_hapi_refugees_png.csv
  format: null
  id: resource_e517cfe7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Refugees & Persons of Concern for Papua New Guinea'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Conflict Event data from HDX HAPI, please see the documentation for
    more information Source: Armed Conflict Location & Event Data Project (ACLED)
    License: By using ACLED data you agree to abide by the Terms of Use and Attribution
    Policy .'
  download_url: https://data.humdata.org/dataset/72a8f7aa-14f9-4eb6-a6aa-011d944595f0/resource/187263a2-6ba1-462e-add6-590836fc23af/download/hdx_hapi_conflict_event_png.csv
  format: null
  id: resource_187263a2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Conflict Events for Papua New Guinea'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'National Risk data from HDX HAPI, please see the documentation for
    more information Source: INFORM License: Creative Commons Attribution International
    (CC BY)'
  download_url: https://data.humdata.org/dataset/72a8f7aa-14f9-4eb6-a6aa-011d944595f0/resource/375581a2-3a71-4dab-abde-77aeec4da743/download/hdx_hapi_national_risk_png.csv
  format: null
  id: resource_375581a2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: National Risk for Papua New Guinea'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Poverty Rate data from HDX HAPI, please see the documentation for
    more information Source: Oxford Poverty & Human Development Initiative License:
    Public Domain / No restrictions (CC0)'
  download_url: https://data.humdata.org/dataset/72a8f7aa-14f9-4eb6-a6aa-011d944595f0/resource/29862cdd-0c37-491c-a42c-ea9440029cf2/download/hdx_hapi_poverty_rate_png.csv
  format: null
  id: resource_29862cdd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Poverty Rate for Papua New Guinea'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Baseline Population data from HDX HAPI, please see the documentation
    for more information Source: OCHA Field Information Services Section (FISS) License:
    Creative Commons Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/72a8f7aa-14f9-4eb6-a6aa-011d944595f0/resource/0e0a2dce-da2b-4ea4-98a8-d2413959ff23/download/hdx_hapi_population_png.csv
  format: null
  id: resource_0e0a2dce
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Geography & Infrastructure: Baseline Population for Papua New Guinea'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rainfall data from HDX HAPI, please see the documentation for more
    information Source: WFP - World Food Programme License: Creative Commons Attribution
    International (CC BY)'
  download_url: https://data.humdata.org/dataset/72a8f7aa-14f9-4eb6-a6aa-011d944595f0/resource/08294313-3f38-410b-95b9-1b801b1de2d4/download/hdx_hapi_rainfall_png.csv
  format: null
  id: resource_08294313
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Climate: Rainfall for Papua New Guinea'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Data Availability Data from HDX HAPI. Each row in this resource represents
    an administrative division for which data is available, by subcategory. Please
    see the documentation for more information Source: HDX HAPI License: Creative
    Commons Attribution for Intergovernmental Organisations'
  download_url: https://data.humdata.org/dataset/72a8f7aa-14f9-4eb6-a6aa-011d944595f0/resource/0a819b89-5fd6-4cf0-ac5a-4b782ad88bc5/download/hdx_hapi_data_availability_png.csv
  format: null
  id: resource_0a819b89
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Metadata: Data Availability for Papua New Guinea'
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-png_hdxapi_hdxhapi_2001
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
  end: '2026-01-31'
  start: '2001-01-01'
temporal_resolution: null
title: HDX HAPI Data for Papua New Guinea
version: null
vulnerability: null
---
