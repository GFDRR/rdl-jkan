---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/unhcr-bgd-2021-jmsna-ref-anon-data-v2-1
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/unhcr-bgd-2021-jmsna-ref-anon-data-v2-1
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ECHO
    url: https://data.humdata.org/dataset/unhcr-bgd-2021-jmsna-ref-anon-data-v2-1
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-bgd-2021-jmsna-ref-anon-data-v2-1
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-bgd-2021-jmsna-ref-anon-data-v2-1
dataset_id: rdls_lss-bgd_unhcr_jointmultisectorneedsasse_2021
description: 'Following the events of August 2017, the Rohingya community were affected
  by displaced. As of August 2021, 900,000 refugees were residing in 34 camps in Ukhiya
  and Teknaf. With the crisis moving into its fifth year, prospects remain uncertain.
  Comprehensive information on the needs and vulnerabilities of affected host communities
  is needed in order to inform the design and implementation of effective inter-sectoral
  programming. Against this background, a Joint Multi-Sector Needs Assessment (J-MSNA)
  was conducted to support detailed humanitarian planning, meeting the multi-sectoral
  needs of affected populations, and to enhance the ability of operational partners
  to meet the strategic aims of donors and coordinating bodies. Building on past J-MSNAs
  and other assessments, the 2021 J-MSNA aimed to provide an accurate snapshot of
  the situation with the specific objectives of (1) providing a comprehensive evidence
  base of the diverse multi-sectoral needs among refugee populations and the host
  community to inform the 2022 Joint Response Plan; (2) providing an analysis of how
  refugee population and host community needs have changed in 2021; and (3) providing
  the basis for a joint multi-stakeholder analysis process. A total of 3,683 households
  were surveyed across the 34 refugee camps in Ukhiya and Teknaf Upazilas. Households
  were sampled from the Office of the United Nations High Commissioner for Refugees''
  (UNHCR) refugee registration database using a stratified random sampling approach,
  with camps as the strata. Household survey data collection took place between 12
  July and 26 August 2021. Each interview was conducted with an adult household representative
  responding on behalf of the household and its members.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/unhcr-bgd-2021-jmsna-ref-anon-data-v2-1]'
details: The data must be requested via the resource download link
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Sample survey data collected via Computer Assisted Telephone Interview
    (CATI) from registered refugees residing in 34 camps in Ukhiya and Teknaf, Cox's
    Bazar, conducted in 2021 to assess multi-sectoral humanitarian needs (food security,
    health, education, WASH, protection, livelihoods, nutrition, NFI) across the Rohingya
    refugee population displaced since August 2017.
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
    name: IOM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: ECHO
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unhcr-bgd-2021-jmsna-ref-anon-data-v2-1
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Multi-sectoral needs assessment capturing food security, health,
      education, and WASH impacts on 900,000 Rohingya refugees affected by 2017 displacement
      crisis
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
- access_url: https://microdata.unhcr.org/index.php/auth/login/?destination=catalog/966/get-microdata
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Clicking 'Download' leads outside HDX where you can request access
    to the data in csv, xlsx & dta formats
  download_url: null
  format: null
  id: resource_f805bf33
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Bangladesh - Joint Multi Sector Needs Assessment: Cox''s Bazar, Rohingya
    Refugee Response - 2021, Refugees'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh - Joint Multi Sector Needs Assessment: Cox''s Bazar, Rohingya
    Refugee Response - 2021, Refugees (Contains information about the dataset''s metadata
    and data)'
  download_url: https://microdata.unhcr.org/index.php/catalog/966/pdf-documentation
  format: null
  id: resource_e201eedf
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
slug: rdls_lss-bgd_unhcr_jointmultisectorneedsasse_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-08-26'
  start: '2021-07-12'
temporal_resolution: null
title: 'Bangladesh - Joint Multi Sector Needs Assessment: Cox''s Bazar, Rohingya Refugee
  Response - 2021, Refugees'
version: null
vulnerability: null
---
