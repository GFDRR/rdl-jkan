---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/unhcr-irq-2017-msna-v2-1
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IMPACT
    url: https://data.humdata.org/dataset/unhcr-irq-2017-msna-v2-1
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-irq-2017-msna-v2-1
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-irq-2017-msna-v2-1
dataset_id: rdls_lss-irq_unhcr_multisectorneedsassessmen_2017
description: 'IMPACT, in collaboration with UNHCR, conducted a fourth-round Multi
  Sector Needs Assessment (MSNA III) of Syrian refugees to provide a household-level
  analysis of sector-specific needs and vulnerabilities in the Kurdistan Region of
  Iraq (KR-I). Building on the findings of previous MSNA, this study assessed any
  continued vulnerabilities. This assessment and its findings aimed to inform the
  development of the Regional Refugee & Resilience Plan (3RP), as well as relevant
  programming within the different sectors.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-irq-2017-msna-v2-1]'
details: The data must be requested via the resource download link
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Household-level survey data collected via phone bank from randomly
    selected UNHCR-registered Syrian refugees across three governorates (Duhok, Erbil,
    Sulaymaniyah) in Kurdistan Region of Iraq. Multi-sector needs assessment evaluated
    food security, shelter, WASH, health, education, livelihoods, and protection vulnerabilities
    to inform the Regional Refugee & Resilience Plan (3RP) programming.
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
- href: https://data.humdata.org/dataset/unhcr-irq-2017-msna-v2-1
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food security needs and vulnerabilities among Syrian refugee population
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
    description: Shelter, WASH, health, education, livelihoods, and protection needs
      among Syrian refugees
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
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://microdata.unhcr.org/index.php/auth/login/?destination=catalog/904/get-microdata
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Clicking 'Download' leads outside HDX where you can request access
    to the data in csv, xlsx & dta formats
  download_url: null
  format: null
  id: resource_7b19f339
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Iraq - Multi-Sector Needs Assessment, 2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Multi-Sector Needs Assessment, 2017 (Contains information about
    the dataset's metadata and data)
  download_url: https://microdata.unhcr.org/index.php/catalog/904/pdf-documentation
  format: null
  id: resource_b731c790
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
slug: rdls_lss-irq_unhcr_multisectorneedsassessmen_2017
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
  end: '2017-09-30'
  start: '2017-08-21'
temporal_resolution: null
title: Iraq - Multi-Sector Needs Assessment, 2017
version: null
vulnerability: null
---
