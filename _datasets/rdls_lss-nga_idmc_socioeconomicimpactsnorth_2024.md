---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Internal Displacement Monitoring Centre (IDMC)
  url: https://data.humdata.org/dataset/socio-economic-impact-of-internal-displacement-in-northwest-nigeria
creator:
  affiliation: null
  email: null
  name: Internal Displacement Monitoring Centre (IDMC)
  url: https://data.humdata.org/dataset/socio-economic-impact-of-internal-displacement-in-northwest-nigeria
dataset_id: rdls_lss-nga_idmc_socioeconomicimpactsnorth_2024
description: 'This dataset contains both quantitative and qualitative data and financial
  information to measure the impacts of internal displacement in Northwest Nigeria
  as a result of conflict and violence. The survey covers both economic and non-economic
  losses for IDPs and host communities and is structured to explore various aspects
  of livelihoods, land access, housing, health, security and education. Methodology:Developed
  in 2019, IDMC''s survey tool collects quantitative and qualitative data and financial
  information to measure the impacts of internal displacement. The survey covers both
  economic and non-economic losses for IDPs and host communities. It is structured
  to explore various aspects of livelihoods, housing, health, security and education.
  The survey allows data to be disaggregated by sex, age, disability status, income
  and education levels, area of origin, duration of displacement and ethnolinguistic
  identity. This helps to reveal overlapping vulnerabilities. The survey also incorporates
  FAO''s land availability tool, which assess land availability, access and tenure
  security, agricultural production, livelihoods and opportunities, as well as social
  cohesion to inform durable solutions in rural and peri urban areas. Data compilation
  process: Data collection for this study was conducted using a combination of random
  walk and respondent-driven sampling techniques. Enumerators employed random walk
  approach to select participants. Primary sources: This data was collected on behalf
  of IDMC and FAO by an external provider, Ipsos Group S.A. Ipsos is a multinational
  market research company. Additional analysis: A proportion-based analysis was conducted
  based on responses received by respondents for each of the survey questions. The
  results of the analysis are currently being compiled in a final report for publication.
  Data limitations: The findings that can be extrapolated from this dataset are not
  nationally representative of the national contexts wherein they were conducted and
  are indicative of the situation of people displaced by disasters living in those
  sites. Geographic coverage: 2 LGA in Sokoto State - Tangaza and Tureta.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/socio-economic-impact-of-internal-displacement-in-northwest-nigeria]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IDMC's standardized survey tool (developed 2019) was administered to
    IDPs and host communities in Northwest Nigeria to collect quantitative and qualitative
    data on displacement impacts. The survey captures both economic and non-economic
    losses across multiple livelihood and social dimensions, with data aggregated
    to measure socioeconomic consequences of conflict-induced displacement.
  sources:
  - id: source_1
    license: null
    name: Internal Displacement Monitoring Centre (IDMC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/socio-economic-impact-of-internal-displacement-in-northwest-nigeria
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from conflict and violence in Northwest
      Nigeria
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
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Economic losses experienced by IDPs and host communities
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
          quantity_kind: currency
          unit: null
        metric: loss
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Socio economic impacts of internal displacement in Northwest Nigeria
    (Excel)
  download_url: https://data.humdata.org/dataset/913a66f3-de86-4a97-ad40-0e89c38da749/resource/6ddafd35-7701-4dc0-866c-915280503b66/download/idmc_nigeria_socioeconomicimpact_idps_06122024_10012025.xlsx
  format: null
  id: resource_6ddafd35
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idmc_nigeria_socioeconomicimpact_idps_06122024_10012025.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-nga_idmc_socioeconomicimpactsnorth_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-01-10'
  start: '2024-12-06'
temporal_resolution: null
title: Socio economic impacts of internal displacement in Northwest Nigeria
version: null
vulnerability: null
---
