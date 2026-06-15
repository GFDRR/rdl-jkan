---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) - Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/somalia-displacement-idps-emergency-trends-tracking-ett-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/somalia-displacement-idps-emergency-trends-tracking-ett-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/somalia-displacement-idps-emergency-trends-tracking-ett-iom-dtm
dataset_id: rdls_hl-som_iom_displacementidpsemergency_2022
description: 'Emergency Trends Tracking (ETT) is a crisis-based tool that tracks sudden
  displacement triggered by specific events or emerging crises. The objective of ETT
  is to help prioritize humanitarian response and to enable partners to deliver rapid
  assistance. Based on previous drought induced displacement patterns, and the ones
  observed since the beginning of the drought, the humanitarian community expects
  that people will move from rural to urban areas in search of humanitarian services.
  Consequently, this ETT tool which concentrates only on drought induced displacements,
  focuses on the main urban centers and surrounding villages for each district. The
  data is collected through Key Informant Interviews (KIIs) at the location level,
  from Sunday to Wednesday every week. All locations assessed are monitored each week..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/somalia-displacement-idps-emergency-trends-tracking-ett-iom-dtm]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: SPI:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Emergency Trends Tracking (ETT) is a crisis-based monitoring tool that
    collects empirical displacement data through IOM DTM standard methodology. Data
    are collected at regular intervals (weekly rounds, R1-R33) from September 2022
    to May 2023 in Bay Region, Somalia, tracking population movements triggered by
    drought-induced humanitarian crises to enable rapid humanitarian response prioritization.
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
- href: https://data.humdata.org/dataset/somalia-displacement-idps-emergency-trends-tracking-ett-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons (IDPs) from drought-induced displacement
      in Bay Region
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
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
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (DTM Somali - Bay region (Drought) - R33 (13 - 18 May 2023))
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/7a789e50-8880-43a8-b63e-15e917ac7d57/download/iom_dtm_ett_baydroughts_tracker_r33.xlsx
  format: null
  id: resource_7a789e50
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R33 (13 - 18 May 2023)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (DTM Somali - Bay region (Drought) - R20 - R32 (11 Feb - 17
    May 2023))
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/f6b6e699-9269-4054-a4dc-3f197f9d6eff/download/iom_dtm_ett_baydroughts_tracker_r20_r32.xlsx
  format: null
  id: resource_f6b6e699
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R20 - R32 (11 Feb - 17 May 2023)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (DTM Somali - Bay region (Drought) - R19 (04 - 10 Feb 2023))
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/4daf722d-b4c8-4eab-b087-dd83c59581f0/download/hdx_dtm_ett_baydroughts_tracker_r19.xlsx
  format: null
  id: resource_4daf722d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R19 (04 - 10 Feb 2023)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (DTM Somali - Bay region (Drought) - R18 (29 - 03 Feb 2023))
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/356f7a34-f4d6-4d22-ada6-b175db8f8510/download/hdx_dtm_ett_baydroughts_tracker_r18.xlsx
  format: null
  id: resource_356f7a34
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R18 (29 - 03 Feb 2023)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (DTM Somali - Bay region (Drought) - R17 (21 - 27 Jan 2023))
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/5931d299-5d26-4737-a6ef-53c3c48ee893/download/hdx_dtm_ett_baydroughts_tracker_r17.xlsx
  format: null
  id: resource_5931d299
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R17 (21 - 27 Jan 2023)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (DTM Somali - Bay region (Drought) - R15 (07 - 12 Jan 2023))
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/23c744be-df37-48a4-887e-05d60dc8d334/download/iom_dtm_ett_baydroughts_tracker_r15_07_12_jan_2023.xlsx
  format: null
  id: resource_23c744be
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R15 (07 - 12 Jan 2023)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (DTM Somali - Bay region (Drought) - R14 (31 Dec 2022 - 05
    Jan 2023))
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/a48b4f99-667f-4b7e-8e0c-92c6c7e5286e/download/om_dtm_ett_baydroughts_tracker_r14_31_dec_05_jan_2023.xlsx
  format: null
  id: resource_a48b4f99
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R14 (31 Dec 2022 - 05 Jan 2023)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (DTM Somali - Bay region (Drought) - R13 (24 - 30 Dec 2022))
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/f7368b8f-3971-4e0c-8632-588501d3271c/download/iom_dtm_ett_baydroughts_round_13_24_30_dec_2022.xlsx
  format: null
  id: resource_f7368b8f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R13 (24 - 30 Dec 2022)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (DTM Somali - Bay region (Drought) - R12 (17 - 22 Dec 2022))
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/188166ae-0396-42cf-b33f-7b2d03472d5c/download/iom_dtm_ett_baydroughts_round_12_17_22_dec_2022.xlsx
  format: null
  id: resource_188166ae
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R12 (17 - 22 Dec 2022)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (DTM Somali - Bay region (Drought) - R11 (10 - 15 Dec 2022))
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/a6956388-2203-486d-940f-049a022e2ca4/download/iom_dtm_ett_baydroughts_tracker_r11_10_15_dec_2022.xlsx
  format: null
  id: resource_a6956388
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R11 (10 - 15 Dec 2022)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (DTM Somali - Bay region (Drought) - R10 (03 - 08 Dec 2022))
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/0e404ae0-2daf-4521-bf37-e6d6d807df03/download/iom_dtm_ett_baydroughts_tracker_r10_03_08_dec_2022.xlsx
  format: null
  id: resource_0e404ae0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R10 (03 - 08 Dec 2022)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (DTM Somali - Bay region (Drought) - R9 (27 Nov - 01 Dec 2022))
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/065b7501-066d-441f-868a-9600670f5914/download/hdx_iom_dtm_ett_baydroughts_tracker_r09_27nov_01dec_2022.xlsx
  format: null
  id: resource_065b7501
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R9 (27 Nov - 01 Dec 2022)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (DTM Somali - Bay region (Drought) - R8 (19 - 24 Nov 2022))
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/4578f67a-bdae-48ba-9fc5-925c6abc3a68/download/iom_dtm_ett_baydroughts_tracker_r08_19nov_24nov_2022.xlsx
  format: null
  id: resource_4578f67a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R8 (19 - 24 Nov 2022)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (This data contains round 7 data.)
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/1dbcdd07-27b7-4aa1-af61-67b48f54ffcd/download/hxl_iom_dtm_ett_baydroughts_tracker_r07_12_nov_17_nov_2022.xlsx
  format: null
  id: resource_1dbcdd07
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R7 (12 - 17 Nov 2022)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (This data contains round 6 data.)
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/ccbd8fdf-5cd1-45f3-ae1a-ccc02a755e47/download/hxl_iom_dtm_ett_baydroughts_tracker_r06_05_nov_10_nov_2022.xlsx
  format: null
  id: resource_ccbd8fdf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R6 (05 - 10 Nov 2022)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In early 2022, as the drought continued to worsen with displacement
    increasing in Somalia, DTM team started to pilot an Emergency Trends Tracking
    (ETT) tool in Gedo region to monitor displacement trends and hotspots in support
    of operational planning. In July 2022, four failed consecutive rainy seasons have
    resulted in 90% of the country experiencing severe drought conditions. Considering
    the extension of the drought, DTM team decided to expand its ETT to Bay region
    as data providers reported significant displacements from June 2022 in the region.
    To avoid duplication/maximization of resources, this expansion was done in close
    coordination with the CCCM Cluster to ensure that the ETT focuses on host community
    locations and IDP sites that are not covered by the CCCM Cluster's New Arrivals
    tracker. This is to avoid duplication and ensure maximization of resources. ETT
    is a crisis-based tool that tracks sudden displacement triggered by specific events
    or emerging crises. The objective of ETT is to help prioritize humanitarian response
    and to enable partners to deliver rapid assistance. Based on previous drought
    induced displacement patterns, and the ones observed since the beginning of the
    drought, the humanitarian community expects that people will move from rural to
    urban areas in search of humanitarian services. Consequently, this ETT tool which
    concentrates only on drought induced displacements, focuses on the main urban
    centers and surrounding villages for each district. The data is collected through
    Key Informant Interviews (KIIs) at the location level, from Sunday to Wednesday
    every week. All locations assessed are monitored each week. The CCCM Cluster New
    Arrivals was established in early 2022 in response to the drought to provide weekly
    updates on new arrivals entering CCCM partner managed IDPs sites. The system allows
    CCCM partners network staff to report daily or weekly on new arrivals in CCCM
    partner managed sites.
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/bd6de894-526c-43b0-8153-530c01f2b1ad/download/hdx_iom_dtm_somalia_ett_r01_r05_17_sep_03_nov_2022.xlsx
  format: null
  id: resource_bd6de894
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R1 to R5 (17 Sep - 03 Nov 2022)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay
    Region - [IOM DTM] (DTM Somali - Bay region (Drought) - R33 (13 - 18 May 2023))
  download_url: https://data.humdata.org/dataset/daea4d46-e36c-49a2-bb79-1acab43d8f21/resource/3e907eca-3e9f-4504-8fdb-505d1c6d70d8/download/iom_dtm_ett_baydroughts_tracker_r33.xlsx
  format: null
  id: resource_3e907eca
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Somali - Bay region (Drought) - R33 (13 - 18 May 2023)
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_iom_displacementidpsemergency_2022
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
  end: '2023-05-18'
  start: '2022-09-17'
temporal_resolution: null
title: Somalia Displacement - [IDPs] - Emergency Trends Tracking (ETT) - Bay Region
  - [IOM DTM]
version: null
vulnerability: null
---
