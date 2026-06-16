---
attributions:
- entity:
    affiliation: null
    email: null
    name: Integrated Phase Classification (IPC)
    url: https://data.humdata.org/dataset/sudan-ipc-2021-2022
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-ipc-2021-2022
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-ipc-2021-2022
dataset_id: rdls_lss-sdn_ochasdn_integratedphaseclassifica_2021
description: 'Latest data shows that an estimated 7.3 million people in Sudan (16%
  of the population analyzed) are in high levels of acute food insecurity (IPC Phase
  3 or above) between April and May (current period) and require urgent action. Of
  these, around 5.5 million people are classified in Crisis (IPC Phase 3) while around
  1.8 million are critically food insecure classified in Emergency (IPC Phase 4).
  The most affected localities of Red Sea State (Halaib and Jubayt-el-maaadin) are
  classified in Emergency (IPC Phase 4). An increase in localized conflicts triggered
  population displacement, which, combined with the deterioration of the economy,
  led to higher than usual levels of acute food insecurity. As a result, the highest
  prevalence of population in Crisis (IPC Phase 3) or worse are observed in North
  Darfur (25%), followed by West Darfur (22%), North Kordofan (20%), South Kordofan
  (20%), Gedarif (19%) and Central, East and South Darfur states, ranging from 17-18%..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sudan-ipc-2021-2022]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IPC classification data aggregated by OCHA Sudan from direct observational
    and anecdotal data collection across Sudan localities. Population counts are classified
    into IPC phases (3-4 representing high acute food insecurity) to quantify food
    insecurity-related impacts on affected populations during April-May assessment
    period.
  sources:
  - id: source_1
    license: null
    name: Integrated Phase Classification (IPC)
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sudan-ipc-2021-2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by acute food insecurity classified by IPC phase
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sudan Integrated Food Security Phase Classification (IPC) ACUTE FOOD
    INSECURITY ANALYSIS APRIL 2021 - FEBRUARY 2022-Issued May 2021
  download_url: https://data.humdata.org/dataset/a6210b6d-12ba-49da-b0e9-79e6d349ffd6/resource/bb62f8f8-d2bd-40a1-b063-4383a537375b/download/sudan-ipc-2021-2022.xlsx
  format: null
  id: resource_bb62f8f8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sudan IPC 2021-2022.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ochasdn_integratedphaseclassifica_2021
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
  end: '2022-03-01'
  start: '2021-05-01'
temporal_resolution: null
title: 'Sudan: Integrated Phase Classification data'
version: null
vulnerability: null
---
