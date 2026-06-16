---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/unhcr-irq-2021-msna-v2-1
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IMPACT
    url: https://data.humdata.org/dataset/unhcr-irq-2021-msna-v2-1
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-irq-2021-msna-v2-1
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-irq-2021-msna-v2-1
dataset_id: rdls_lss-irq_unhcr_multisectorneedsassessmen_2021
description: 'IMPACT, in collaboration with UNHCR, conducted a sixth round of the
  Multi-Sector Needs Assessment (MSNA) of refugees in Iraq who live in and out of
  formal camps. The aim of the MSNA 2021 is to provide a household-level analysis
  of sector-specific needs and vulnerabilities of Syrian refugee and host community
  households. The MSNA 2021 sampling consists of samples of Syrian refugees in KR-I
  (where most Syrian refugees live), but also Anbar, Baghdad, Kirkuk and Ninewa (referred
  to as Centre-South, where most Syrian refugee households outside of KRI live), as
  well as host community households in KR-I given the high concentration of Syrian
  refugees in KR-I. Host communities were sampled to offer comparison and to include
  host communities in 3RP planning on the basis of identified needs and vulnerabilities
  by the MSNA. This assessment and its findings aim to support the prioritization
  across and within different sectors and is to be used as a basis for developing
  the 3RP Regional Refugee & Resilience Plan (3RP) 2022 This research sought to respond
  to the information need on multi-sectoral needs, movement intentions and the impact
  of COVID-19 on refugees'' lives, thus assisting humanitarian actors in organizing
  their response to protracted displacement of Syrian refugees across Iraq in the
  time of COVID-19.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-irq-2021-msna-v2-1]'
details: The data must be requested via the resource download link
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Household and individual-level survey data collected via computer-assisted
    personal interviews (CAPI) from Syrian refugee and host community samples across
    Iraq (KR-I, Anbar, Baghdad, Kirkuk, Ninewa). Data aggregated to provide sector-specific
    needs assessments across education, food security, health, livelihoods, protection,
    shelter, and WASH, representing post-displacement humanitarian impact.
  sources:
  - id: source_1
    license: null
    name: UNHCR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: IMPACT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unhcr-irq-2021-msna-v2-1
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Multi-sector needs of Syrian refugee and host community households
      affected by displacement and humanitarian crisis
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
  - asset_category: economic_indicator
    asset_dimension: index
    description: Food security, livelihoods, and economic vulnerability indicators
      for refugee and host populations
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
          quantity_kind: currency
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
purpose: null
referenced_by: []
resources:
- access_url: https://microdata.unhcr.org/index.php/auth/login/?destination=catalog/915/get-microdata
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Clicking 'Download' leads outside HDX where you can request access
    to the data in csv, xlsx & dta formats
  download_url: null
  format: null
  id: resource_604e7c55
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Iraq - Multi-Sector Needs Assessment, 2021
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Multi-Sector Needs Assessment, 2021 (Contains information about
    the dataset's metadata and data)
  download_url: https://microdata.unhcr.org/index.php/catalog/915/pdf-documentation
  format: null
  id: resource_8229fc01
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Codebook
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-irq_unhcr_multisectorneedsassessmen_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-09-21'
  start: '2021-08-18'
temporal_resolution: null
title: Iraq - Multi-Sector Needs Assessment, 2021
version: null
vulnerability: null
---
