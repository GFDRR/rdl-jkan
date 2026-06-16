---
attributions:
- entity:
    affiliation: null
    email: null
    name: Integrated Food Security Phase Classification (IPC)
    url: https://data.humdata.org/dataset/south-sudan-integrated-food-security-phase-classification-and-population-by-state-and-county
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA South Sudan
  url: https://data.humdata.org/dataset/south-sudan-integrated-food-security-phase-classification-and-population-by-state-and-county
creator:
  affiliation: null
  email: null
  name: OCHA South Sudan
  url: https://data.humdata.org/dataset/south-sudan-integrated-food-security-phase-classification-and-population-by-state-and-county
dataset_id: rdls_lss-ssd_ochassd_integratedfoodsecuritypha_2017
description: 'South Sudan Integrated Food Security Phase classification and population
  by state and County. The Integrated Food Security Phase Classification (IPC), also
  known as IPC scale, is a tool for improving food security analysis and decision-making.
  It is a standardized scale that integrates food security, nutrition and livelihood
  information into a statement about the nature and severity of a crisis and implications
  for strategic response. The IPC was originally developed for use in Somalia by the
  United Nations Food and Agriculture Organization''s Food Security Analysis Unit
  (FSAU). Several national governments and international agencies, including CARE
  International, European Commission Joint Research Centre (EC JRC), Food and Agricultural
  Organization of the United Nations (FAO), USAID/FEWS NET, Oxfam GB, Save the Children
  UK/US, and United Nations World Food Programme (WFP), have been working together
  to adapt it to other food security contexts. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/south-sudan-integrated-food-security-phase-classification-and-population-by-state-and-county]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IPC classifications and population figures aggregated by state and
    county from multiple sources using sample survey methodology. The IPC scale standardizes
    food security analysis across geographic units to inform strategic humanitarian
    response decisions.
  sources:
  - id: source_1
    license: null
    name: Integrated Food Security Phase Classification (IPC)
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/south-sudan-integrated-food-security-phase-classification-and-population-by-state-and-county
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by Integrated Food Security Phase (IPC) severity
      levels indicating food insecurity and livelihood crisis
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
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan - Integrated Food Security Phase classification and population
    by state and County (Excel)
  download_url: https://data.humdata.org/dataset/efb5d747-54b4-485b-8408-e0b77f341fff/resource/ffdc3b97-34f1-4e2a-ab31-ed3700b9fc81/download/ipc_populations_by_state_county.xlsx
  format: null
  id: resource_ffdc3b97
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IPC_Populations_by_State_County.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ssd_ochassd_integratedfoodsecuritypha_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-07-31'
  start: '2017-01-01'
temporal_resolution: null
title: South Sudan - Integrated Food Security Phase classification and population
  by state and County
version: null
vulnerability: null
---
