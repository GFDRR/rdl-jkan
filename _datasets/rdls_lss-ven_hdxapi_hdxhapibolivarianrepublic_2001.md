---
attributions:
- entity:
    affiliation: null
    email: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    url: https://data.humdata.org/dataset/hdx-hapi-ven
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/hdx-hapi-ven
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR - The UN Refugee Agency
    url: https://data.humdata.org/dataset/hdx-hapi-ven
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP - World Food Programme
    url: https://data.humdata.org/dataset/hdx-hapi-ven
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Venezuela
    url: https://data.humdata.org/dataset/hdx-hapi-ven
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-ven
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-ven
dataset_id: rdls_lss-ven_hdxapi_hdxhapibolivarianrepublic_2001
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-ven]'
details: HDX HAPI is refreshed daily, but the source datasets may have different update
  schedules. Please refer to the source datasets for each subcategory to verify their
  specific update frequency.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: HDX HAPI aggregates standardized humanitarian indicators from multiple
    UN and international organizations (ACLED, UNHCR, WFP, OCHA, INFORM) into a unified
    API for Venezuela. Data includes observed rainfall measurements, conflict event
    records with affected populations, refugee/returnee statistics, and humanitarian
    needs assessments. The dataset integrates these sources to support automated humanitarian
    decision-making workflows.
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
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: OCHA Venezuela
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-ven
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Affected population from conflict events
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by humanitarian needs including food insecurity
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
  download_url: https://data.humdata.org/dataset/8afc4aae-bac9-4725-88c5-362a587f0fd0/resource/b8e074f0-0665-4d19-bfe4-c58e48bdeffb/download/hdx_hapi_refugees_ven.csv
  format: null
  id: resource_b8e074f0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Refugees & Persons of Concern for Venezuela (Bolivarian
    Republic of)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Returnees data from HDX HAPI, please see the documentation for more
    information Source: UNHCR - The UN Refugee Agency License: Creative Commons Attribution
    for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/8afc4aae-bac9-4725-88c5-362a587f0fd0/resource/998db825-bf1b-400e-b821-df2c3bc946c0/download/hdx_hapi_returnees_ven.csv
  format: null
  id: resource_998db825
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Returnees for Venezuela (Bolivarian Republic of)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Humanitarian needs data from HDX HAPI, please see the documentation
    for more information Source: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
    License: Creative Commons Attribution for Intergovernmental Organisations (CC
    BY-IGO)'
  download_url: https://data.humdata.org/dataset/8afc4aae-bac9-4725-88c5-362a587f0fd0/resource/439fa6b1-4222-4d3b-b65e-95f5ac0a498b/download/hdx_hapi_humanitarian_needs_ven.csv
  format: null
  id: resource_439fa6b1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Humanitarian Needs for Venezuela (Bolivarian Republic of)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Operational Presence data from HDX HAPI, please see the documentation
    for more information Source: OCHA Venezuela License: Creative Commons Attribution
    International (CC BY)'
  download_url: https://data.humdata.org/dataset/8afc4aae-bac9-4725-88c5-362a587f0fd0/resource/6c1d8ef2-c81e-4a04-9eb9-d909491002e1/download/hdx_hapi_operational_presence_ven.csv
  format: null
  id: resource_6c1d8ef2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Operational Presence for Venezuela (Bolivarian Republic
    of)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Funding data from HDX HAPI, please see the documentation for more
    information Source: OCHA Financial Tracking System (FTS) License: Creative Commons
    Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/8afc4aae-bac9-4725-88c5-362a587f0fd0/resource/4a643b65-25ea-480f-974f-fe48335eaedc/download/hdx_hapi_funding_ven.csv
  format: null
  id: resource_4a643b65
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Funding for Venezuela (Bolivarian Republic of)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Conflict Event data from HDX HAPI, please see the documentation for
    more information Source: Armed Conflict Location & Event Data Project (ACLED)
    License: By using ACLED data you agree to abide by the Terms of Use and Attribution
    Policy .'
  download_url: https://data.humdata.org/dataset/8afc4aae-bac9-4725-88c5-362a587f0fd0/resource/c7d45bbb-7d1a-47b9-9960-2ab221d0cfcc/download/hdx_hapi_conflict_event_ven.csv
  format: null
  id: resource_c7d45bbb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Conflict Events for Venezuela (Bolivarian Republic
    of)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'National Risk data from HDX HAPI, please see the documentation for
    more information Source: INFORM License: Creative Commons Attribution International
    (CC BY)'
  download_url: https://data.humdata.org/dataset/8afc4aae-bac9-4725-88c5-362a587f0fd0/resource/7074633c-8ec8-4263-bfc8-b82a0bc437c1/download/hdx_hapi_national_risk_ven.csv
  format: null
  id: resource_7074633c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: National Risk for Venezuela (Bolivarian Republic
    of)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Food Prices & Market Monitor data from HDX HAPI, please see the documentation
    for more information Source: WFP - World Food Programme License: Creative Commons
    Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/8afc4aae-bac9-4725-88c5-362a587f0fd0/resource/d866d78f-a326-4ce3-a27e-f443a6a63b21/download/hdx_hapi_food_price_ven.csv
  format: null
  id: resource_d866d78f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Food Prices & Market Monitor for Venezuela
    (Bolivarian Republic of)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Baseline Population data from HDX HAPI, please see the documentation
    for more information Source: OCHA Venezuela License: Creative Commons Attribution
    for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/8afc4aae-bac9-4725-88c5-362a587f0fd0/resource/c9e0ec44-bb6f-4f76-97a0-8e5aab332914/download/hdx_hapi_population_ven.csv
  format: null
  id: resource_c9e0ec44
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Geography & Infrastructure: Baseline Population for Venezuela (Bolivarian
    Republic of)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rainfall data from HDX HAPI, please see the documentation for more
    information Source: WFP - World Food Programme License: Creative Commons Attribution
    International (CC BY)'
  download_url: https://data.humdata.org/dataset/8afc4aae-bac9-4725-88c5-362a587f0fd0/resource/3b35ea71-f24b-4bc3-b800-91dcd38bb2ff/download/hdx_hapi_rainfall_ven.csv
  format: null
  id: resource_3b35ea71
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Climate: Rainfall for Venezuela (Bolivarian Republic of)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Data Availability Data from HDX HAPI. Each row in this resource represents
    an administrative division for which data is available, by subcategory. Please
    see the documentation for more information Source: HDX HAPI License: Creative
    Commons Attribution for Intergovernmental Organisations'
  download_url: https://data.humdata.org/dataset/8afc4aae-bac9-4725-88c5-362a587f0fd0/resource/dd41d43c-677f-438b-a061-66fbb79d1444/download/hdx_hapi_data_availability_ven.csv
  format: null
  id: resource_dd41d43c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Metadata: Data Availability for Venezuela (Bolivarian Republic of)'
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ven_hdxapi_hdxhapibolivarianrepublic_2001
spatial:
  bbox: null
  centroid: null
  countries:
  - VEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2028-12-31'
  start: '2001-01-01'
temporal_resolution: null
title: HDX HAPI Data for Venezuela (Bolivarian Republic of)
version: null
vulnerability: null
---
