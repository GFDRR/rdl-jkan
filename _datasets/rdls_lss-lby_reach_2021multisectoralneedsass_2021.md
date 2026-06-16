---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/reach-libya-2021-multi-sectoral-needs-assessment-libyan-population-data-summaries
creator:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/reach-libya-2021-multi-sectoral-needs-assessment-libyan-population-data-summaries
dataset_id: rdls_lss-lby_reach_2021multisectoralneedsass_2021
description: 'The data summaries here include the individual indicator results from
  the 2021 Libyan population Multi-Sectoral Needs Assessment. The data can be requested
  from HDX connect through the ''REACH Libya 2021 Multi-Sectoral Needs Assessment
  (Libyan Population) - Dataset'' page. The needs assessment covers protection, health,
  WASH, Shelter and NFI, Education, food security, livelihoods, cash, and markets.
  A total of 8871 household surveys were completed across 45 baladiyas (ADM3) in Libya.
  Due to ongoing COVID-19 restrictions and safety measures, all surveys took place
  over the phone. A non-probability, quota based sampling methodology was established,
  to ensure an accurate and robust cross-section of the Libyan population. Quotas
  were established for baladiyas (quota 1) and sub-groups within the population (non-displaced,
  IDPs, and returnees) (quota 2). Findings presented are not representative, and should
  be read only as indicative. Sampling of respondents was done primarily through Civil
  Society Organisation (CSO) networks, municipalities, International Non-Government
  Organisation (INGO) partners, and various local committees. 1000 of the total number
  of surveys were sampled through Random Digit Dialing (RDD) by a Libyan company specialized
  in this methodology. Additional sampling and data collection was done by international
  and national NGO partners and UN programmes. Quantitative data collection took place
  between 14 June and 31 July.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/reach-libya-2021-multi-sectoral-needs-assessment-libyan-population-data-summaries]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: A non-probability household survey was conducted by REACH Initiative
    across 45 administrative divisions (baladiyas) in Libya in 2021, with 8,871 telephone-based
    interviews collecting multi-sectoral needs data on food security, livelihoods,
    health, WASH, shelter, and protection. The data summaries present aggregated indicator
    results by sector and geography, representing post-crisis humanitarian needs assessment
    outputs.
  sources:
  - id: source_1
    license: null
    name: REACH Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/reach-libya-2021-multi-sectoral-needs-assessment-libyan-population-data-summaries
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food security needs and affected population from multi-sectoral assessment
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
    description: Livelihood and cash needs from multi-sectoral assessment
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: REACH Libya 2021 Multi-Sectoral Needs Assessment (Libyan Population)
    - Data summaries (2021 LBY MSNA_data summaries.xlsx)
  download_url: https://data.humdata.org/dataset/e3363a0b-9490-476a-beee-ab919985e4fa/resource/5f47fd16-0904-457b-b27f-11183715769b/download/2021-lby-msna_data-summaries.xlsx
  format: null
  id: resource_5f47fd16
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2021 LBY MSNA_data summaries.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-lby_reach_2021multisectoralneedsass_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - LBY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-07-31'
  start: '2021-06-14'
temporal_resolution: null
title: REACH Libya 2021 Multi-Sectoral Needs Assessment (Libyan Population) - Data
  summaries
version: null
vulnerability: null
---
