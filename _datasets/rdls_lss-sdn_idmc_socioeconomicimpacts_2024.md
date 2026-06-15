---
attributions:
- entity:
    affiliation: null
    email: null
    name: Norwegian Refugee Council (NRC)
    url: https://data.humdata.org/dataset/socio-economic-impacts-of-internal-displacement-in-sudan
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Internal Displacement Monitoring Centre (IDMC)
  url: https://data.humdata.org/dataset/socio-economic-impacts-of-internal-displacement-in-sudan
creator:
  affiliation: null
  email: null
  name: Internal Displacement Monitoring Centre (IDMC)
  url: https://data.humdata.org/dataset/socio-economic-impacts-of-internal-displacement-in-sudan
dataset_id: rdls_lss-sdn_idmc_socioeconomicimpacts_2024
description: 'This dataset, collected by the NRC with local partners, provides quantitative
  and qualitative data and financial information to assess the economic and non-economic
  impacts of internal displacement due to conflict and violence in eight Sudanese
  states. Utilizing IDMC''s socioeconomic impact assessment tool combined with NRC''s
  multi-sectoral needs assessment tool, the survey explores livelihoods, housing,
  health, security, and education for both internally displaced persons (IDPs) and
  host communities. The methodology, developed in 2019, allows for data disaggregation
  by sex, age, disability, income, education, origin, displacement duration, and ethnolinguistic
  identity to identify overlapping vulnerabilities. Data was compiled using systematic
  random sampling, random walk, and respondent-driven sampling with a 95% confidence
  level and 5% margin of error, aiming for gender balance. While not nationally representative,
  the findings are representative of displaced populations in the surveyed sites.
  The report, ''Bursting at the Seams: The Impact of War and Displacement on Sudan''s
  Eastern Cities,'' available on the NRC website, presents a proportion-based analysis
  of the collected data. The initial data collection covered Red Sea, Kassala, Gedeaf,
  Northern, White Nile, and Blue Nile states, with a second round focusing on River
  Nile and Sennar. Specific localities within these states are also covered. A proportion-based
  analysis was conducted based on responses received by respondents for each of the
  survey questions. The results of the analysis have been published and can be found
  here: https://www.nrc.no/resources/reports/bursting-at-the-seams-the-impact-of-war-and-displacement-on-sudans-eastern-cities.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/socio-economic-impacts-of-internal-displacement-in-sudan]'
details: The findings that can be extrapolated from this dataset are not nationally
  representative of the national contexts wherein they were conducted but can be considered
  representative of the situation of people displaced by disasters living in those
  sites.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Survey data collected by NRC with local partners across eight Sudanese
    states using IDMC's socioeconomic impact assessment tool combined with NRC's multi-sectoral
    needs assessment methodology. The dataset captures quantitative and qualitative
    impacts of internal displacement on IDPs and host communities, disaggregated by
    sex, age, and disability status, covering livelihoods, housing, health, security,
    and education sectors.
  sources:
  - id: source_1
    license: null
    name: Internal Displacement Monitoring Centre (IDMC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Norwegian Refugee Council (NRC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/socio-economic-impacts-of-internal-displacement-in-sudan
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from conflict and violence in Sudan
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
  - asset_category: population
    asset_dimension: population
    description: Host communities affected by internal displacement
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
  description: 'Sudan: Socio Economic Impacts of Internal Displacement (Excel)'
  download_url: https://data.humdata.org/dataset/e064196f-3bb4-463f-b1ef-239e54a1be14/resource/3718c290-ab89-456e-a444-e1617d8c578d/download/idmc_sudan_socioeconomicimpact_idps_06122024_10012025.xlsx
  format: null
  id: resource_3718c290
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idmc_sudan_socioeconomicimpact_idps_06122024_10012025.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_idmc_socioeconomicimpacts_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-09-05'
  start: '2024-08-13'
temporal_resolution: null
title: 'Sudan: Socio Economic Impacts of Internal Displacement'
version: null
vulnerability: null
---
