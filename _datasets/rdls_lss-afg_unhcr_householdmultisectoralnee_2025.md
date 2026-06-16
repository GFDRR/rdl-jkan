---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR Afghanistan
    url: https://data.humdata.org/dataset/unhcr-afg-2025-hmsna
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-afg-2025-hmsna
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-afg-2025-hmsna
dataset_id: rdls_lss-afg_unhcr_householdmultisectoralnee_2025
description: 'The Household Multi-Sectoral Needs Assessment (HMNA) Mid-Year 2025 was
  carried out by UNHCR Afghanistan between April and June 2025 across all 34 provinces.
  The survey aimed to identify families in need of cash assistance and to capture
  the evolving needs of diverse population groups, including host communities, refugees,
  internally displaced people (IDPs), returnees, and asylum-seekers. The assessment
  covers multiple sectors such as basic needs, protection, shelter, WASH, education,
  legal assistance, and community services. Findings provide evidence to guide UNHCR''s
  operational response, particularly in addressing urgent vulnerabilities and informing
  solutions related to cash-based interventions, voluntary repatriation, sustainable
  reintegration, and local integration.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-afg-2025-hmsna]'
details: The data must be requested via the resource download link
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: UNHCR conducted a household survey across all 34 Afghan provinces from
    April-June 2025 using simple random sampling to assess multi-sectoral needs of
    diverse population groups. The assessment captures humanitarian impact indicators
    across basic needs, protection, shelter, WASH, education, and livelihoods to guide
    operational response and cash assistance targeting.
  sources:
  - id: source_1
    license: null
    name: UNHCR Afghanistan
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unhcr-afg-2025-hmsna
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Multi-sectoral needs of affected populations including food insecurity,
      shelter, WASH, and protection
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
    description: Multi-sectoral needs of affected populations including food insecurity,
      shelter, WASH, and protection
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
- access_url: https://microdata.unhcr.org/index.php/auth/login/?destination=catalog/1398/get-microdata
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Clicking 'Download' leads outside HDX where you can request access
    to the data in csv, xlsx & dta formats
  download_url: null
  format: null
  id: resource_d3152127
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Afghanistan - Household Multi-Sectoral Need Assessment (MSNA) - 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Household Multi-Sectoral Need Assessment (MSNA) - 2025
    (Contains information about the dataset's metadata and data)
  download_url: https://microdata.unhcr.org/index.php/catalog/1398/pdf-documentation
  format: null
  id: resource_a679ab7e
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
slug: rdls_lss-afg_unhcr_householdmultisectoralnee_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-06-30'
  start: '2025-04-21'
temporal_resolution: null
title: Afghanistan - Household Multi-Sectoral Need Assessment (MSNA) - 2025
version: null
vulnerability: null
---
