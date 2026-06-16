---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) - Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/somalia-displacement-idps-emergency-trends-tracking-ett-since-oct2023-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/somalia-displacement-idps-emergency-trends-tracking-ett-since-oct2023-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/somalia-displacement-idps-emergency-trends-tracking-ett-since-oct2023-iom-dtm
dataset_id: rdls_lss-som_iom_displacementidpsemergency_2023
description: 'In response to the Somalia''s severe drought beginning in November 2021,
  DTM Somalia launched an Emergency Trends Tracking (ETT) tool first in Gedo and Bay
  regions in 2022, and subsequently in Hiraan, Banadir and Middle Shabelle regions
  in 2023 to monitor drought related displacement trends and hotspots in support of
  operational planning. However, during the first half of 2023, conflict and flooding
  displacements have been significant. Therefore, DTM restructured its ETT tool to
  capture multi-shock displacements (drought, flood, conflict and other) from October
  2023. In April 2024, ETT was conducted to monitor displacements movements during
  the Gu rainy season. This latest round of ETT was initiated in February 2025 to
  monitor displacement movements during the Jilaal dry season. ETT is a crisis-based
  tool that tracks sudden displacement triggered by specific events or emerging crises.
  The objective of ETT is to help prioritize humanitarian response and to enable partners
  to deliver rapid assistance.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/somalia-displacement-idps-emergency-trends-tracking-ett-since-oct2023-iom-dtm]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: DTM Somalia conducted systematic ground assessments of settlements
    across Gedo, Bay, Hiraan, Banadir, and Middle Shabelle regions, initially tracking
    drought-related displacement from November 2021, then expanding to capture multi-shock
    displacements (drought, flood, conflict) from October 2023 onwards. Data collection
    involved weekly monitoring of new arrivals and displacement trends at settlement
    level, with results aggregated by region, district, and operational zone to support
    humanitarian operational planning.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) - Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-displacement-idps-emergency-trends-tracking-ett-since-oct2023-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from drought-related displacement in
      Somalia
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
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from flood-related displacement in Somalia
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
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from conflict-related displacement in
      Somalia
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_3
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
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://dtm.iom.int/sites/g/files/tmzbdl1461/files/DTM%20Methodological%20Framework%20-%202nd%20Edition%202022_0.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This latest round of Emergency Trends Tracking was initiated in February
    2025 to monitor displacement movements during the Jilaal dry season. Since Feb
    2025, DTM teams have collected data in 25 districts: Afgooye, Afmadow, Baardheere,
    Baidoa, Balcad, Belet Weyne, Belet Xaawo, Bu''Aale, Bulo Burto, Cabudwaaq, Dayniile,
    Dhuusamarreeb, Diinsoor, Doolow, Gaalkacyo, Garoowe, Hodan, Jamaame, Jowhar, Kahda,
    Kismaayo, Luuq, Qansax Dheere, Waajid, and Xudur. However, due to operational
    challenges, Jowhar district was not assessed in week 9 (April 5 to 9, 2025), Cabudwaaq
    and Dhuusamarreeb districts in week 13 (May 3 to 7, 2025), and Jamaame district
    in week 16 (May 24 to 28, 2025), week 18 (June 8 to 11, 2025), and week 19 (June
    14 to 18, 2025). Starting week 22 (5 - 9 July, 2025), data is collected in 15
    districts due to limited funding: Afgooye, Baardheere, Baidoa, Balcad, Belet Weyne,
    Belet Xaawo, Bulo Burto, Dayniile, Diinsoor, Doolow, Jowhar, Kahda, Kismaayo,
    Qansax Dheere, and Xudur. In week 25 (July 26 to 30, 2025), Belet Xaawo district
    was not assessed due to the ongoing conflict. Due to a combination of limited
    funding and operational challenges in identifying the five priority districts,
    there has been a data collection gap from August 2 to 20, 2025. Starting Week
    26 (August 23 to 27, 2025), data has been collected in five districts: Baidoa,
    Dayniile, Diinsoor, Doolow, and Kahda. The latest assessment was conducted from
    January 24 to 28, 2026. ETT is a crisis-based tool that tracks sudden displacement
    triggered by specific events or emerging crises. The objective of ETT is to help
    prioritize humanitarian response and to enable partners to deliver rapid assistance.
    Based on previous shock-induced displacement patterns, the humanitarian community
    expects that people will continue to move toward urban areas in search of humanitarian
    services. Consequently, the ETT coverage focuses on the main urban centers and
    surrounding villages for each assessed district. The data is collected through
    Key Informant Interviews (KIIs) at the location level, from Saturday to Wednesday,
    every week. It includes information on new arrivals, numbers and demographics
    of IDPs, reasons for displacement, intentions, humanitarian assistance and priority
    needs, among others. To facilitate the joint analysis of the CCCM (Camp Coordination
    and Camp Management) Cluster''s New Arrivals Tracker (NAT) and ETT data, the assistance
    and needs indicators are identical in both tools.'
  download_url: https://data.humdata.org/dataset/7f9b9d5c-f629-441a-80d2-109ec30efca4/resource/1a13db39-bce9-4565-845c-ad3299206dfd/download/iom_dtm_ett_som_tracker_sincefeb2025_w48.xlsx
  format: null
  id: resource_1a13db39
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somalia ETT Tracker Since February 2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This latest round of Emergency Trends Tracking was initiated in April
    2024 to monitor displacements movements during the Gu rainy season. Districts
    covered in this round include Afgooye, Afmadow, Baardheere, Baidoa, Balcad, Belet
    Weyne, Gaalkacyo, Garoowe, Jamaame, Jowhar, Kismaayo, and Luuq.
  download_url: https://data.humdata.org/dataset/7f9b9d5c-f629-441a-80d2-109ec30efca4/resource/e8db9f1f-1797-40b5-9e72-68ebf0bc28a7/download/iom_dtm_ett_som_tracker_sinceapr2024_r40_hdx.xlsx
  format: null
  id: resource_e8db9f1f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somalia ETT Tracker April to December 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In response to the Somalia's severe drought beginning in November 2021,
    DTM Somalia launched an Emergency Trends Tracking (ETT) tool first in Gedo and
    Bay regions in 2022, and subsequently in Hiraan, Banadir and Middle Shabelle regions
    in 2023 to monitor drought related displacement trends and hotspots in support
    of operational planning. However, during the first half of 2023, conflict and
    flooding displacements have been significant. Therefore, DTM restructured its
    ETT tool to capture multi-shock displacements (drought, flood, conflict and other)
    from October 2023. ETT is a crisis-based tool that tracks sudden displacement
    triggered by specific events or emerging crises. The objective of ETT is to help
    prioritize humanitarian response and to enable partners to deliver rapid assistance.
  download_url: https://data.humdata.org/dataset/7f9b9d5c-f629-441a-80d2-109ec30efca4/resource/d6bb47fa-633b-47cf-8cb0-eb35c5687ff7/download/iom_dtm_ett_som_tracker_sinceoct2023_2024_w8_hdx.xlsx
  format: null
  id: resource_d6bb47fa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somalia ETT Tracker October 2023 to February 2024
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-som_iom_displacementidpsemergency_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-28'
  start: '2023-10-07'
temporal_resolution: null
title: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT)
version: null
vulnerability: null
---
