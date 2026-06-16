---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/burundi-displacement-data-emergency-event-tracking-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/burundi-displacement-data-emergency-event-tracking-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/burundi-displacement-data-emergency-event-tracking-iom-dtm
dataset_id: rdls_lss-bdi_iom_displacementdataemergency_2018
description: 'The DTM Emergency Tracking activated on an ad hoc basis. Only Emergency
  situations which cause significant damage and require an immediate response or cause
  displacement taken into account.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/burundi-displacement-data-emergency-event-tracking-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM field teams conduct weekly emergency event tracking across
    Burundi's administrative divisions, collecting post-event damage assessments for
    residential buildings, infrastructure, and agricultural assets triggered by floods
    and convective storms. Data is compiled into weekly and monthly Excel files with
    standardized damage classification categories (total destruction, partial destruction,
    roof damage, inundation) and counts of affected assets by location and emergency
    type.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/burundi-displacement-data-emergency-event-tracking-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Count of residential buildings totally destroyed, partially destroyed,
      or damaged by flooding
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Infrastructure damage including schools, health facilities, bridges,
      roads, water systems, and markets from flooding
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Agricultural asset loss including destroyed fields and crops from
      flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Count of residential buildings damaged (roofs blown off) by convective
      storms
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Infrastructure damage including electric poles and other structures
      from convective storms
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_5
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
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
  description: "Entre le mois de Janvier et Mars 2025, le changement climatique et\
    \ les catastrophes sont survenus au Burundi et ont affect\xE9 69 430 personnes,\
    \ dont 2 144 personnes d\xE9plac\xE9es. Les principales provinces affect\xE9es\
    \ au cours de cette p\xE9riode ont \xE9t\xE9 Kirundo (20 529 personnes fect\xE9\
    es), Ngozi (12 289 personnes affect\xE9es), Muyinga (9 050 personnes affect\xE9\
    es) et Gitega (5 021 personnes affect\xE9es). Ces catastrophes ont caus\xE9 un\
    \ impact humain grave, d\xE9truit 1 176 maisons, 137 infrastructures ont \xE9\
    t\xE9 endommag\xE9es, et les cultures ont \xE9t\xE9 d\xE9truites, affectant environ\
    \ 112 652 m\xE9nages dans le pays. Du 01 Avril au 14 avril 2025, la DTM a identifi\xE9\
    \ 11,854 personnes affect\xE9es dont 1,908 personnes d\xE9plac\xE9es par la gr\xEA\
    le, les pluies torrentielles et les vents violents dans la province de Kirundo,\
    \ Bujumbura, Cibitoke, Makamba, et Rumonge. Du 15 au 21 Avril, la DTM a identifi\xE9\
    \ 1,886 personnes affect\xE9es dont 481 personnes d\xE9plac\xE9s par la gr\xEA\
    le, les pluies torrentielles et les vents violents dans les provinces de Bujumbura,\
    \ Rumonge, Muyinga, Bujumbura Mairie et Makamba. From May 1 to 14, 2025, 4,169\
    \ individuals were affected, and 433 individuals were displaced. In June 2025,\
    \ 304 individuals were affected, and 59 individuals were displaced. In September\
    \ and October, a total of 8,790 individuals were affected with 2,454 of them being\
    \ internally displaced."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/44f99c73-b57f-4386-a35e-da95dfdf505d/download/dtm-burundi-jan-nov-2025-emergency-event-tracking.xlsx
  format: null
  id: resource_44f99c73
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Jan - Nov 2025 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Du 29 d\xE9cembre 2024 au 4 janvier 2025, la DTM a identifi\xE9 3\
    \ 266 personnes affect\xE9es (536 m\xE9nages) dont 1 147 personnes d\xE9plac\xE9\
    es (166 m\xE9nages) par les pluies torrentielles et les vents violents dans la\
    \ province de Rutana."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/3e79b24f-845e-433b-a98a-4bcec853d7ac/download/dataset_emergency_2024_public.xlsx
  format: null
  id: resource_3e79b24f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_Jan - Dec 2024 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a identifi\xE9 2 785 personnes affect\xE9es (535 m\xE9nages)\
    \ dont 141 personnes d\xE9plac\xE9es (27 m\xE9nages) par les les pluies torrentielles\
    \ et la gr\xEAle dans les provinces de Kayanza, Makamba, Gitega, Cankuzo et Rutana."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/d743b4b4-35d7-4e4d-80b9-18807b5df0b8/download/suivi_des_urgences_21_27_janv_2024_to_be_shared_hdx.xlsx
  format: null
  id: resource_d743b4b4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_21_27_Janvier_2024 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a recens\xE9 un total de 20 951 personnes affect\xE9es et 2\
    \ 424 personnes d\xE9plac\xE9es en raison de diverses urgences survenues en Burundi.\
    \ Ces urgences, comprenant des vents violents et des pluies torrentielles, ont\
    \ \xE9t\xE9 particuli\xE8rement pr\xE9valentes dans les provinces de Bubanza,\
    \ Ruyigi, Muyinga, et Cankuzo"
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/59c7a096-f2bb-4d53-97ed-3b6f74e60bdd/download/suivi_des_urgences_14_20_janv_2024_hdx.xlsx
  format: null
  id: resource_59c7a096
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_14_20_Janvier_2024 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a identifi\xE9 6 861 personnes affect\xE9es, dont 453 personnes\
    \ d\xE9plac\xE9es par les glissements de terrain, les pluies torrentielles, les\
    \ inondations et les vents violents dans les provinces de Bujumbura Rural, Makamba,\
    \ Gitega, Cibitoke et Bururi."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/7ceda1c5-babe-4c92-b534-beab34692123/download/suivi_des_urgences_08_13_janv_2024_hdx.xlsx
  format: null
  id: resource_7ceda1c5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_8_13_Janvier_2024 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a identifi\xE9 34 602 personnes affect\xE9es dont 4 435 personnes\
    \ d\xE9plac\xE9es par les pluies torrentielles dans les provinces de Bujumbura\
    \ Rural, Cankuzo, Muyinga, Ruyigi, Cibitoke, et Bubanza."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/40804d19-7198-4550-a05b-44d8f9808779/download/suivi_des_urgences_01_07_janv_2024_public-hdx.xlsx
  format: null
  id: resource_40804d19
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_1_7_Janvier_2024 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a identifi\xE9 10 767 personnes affect\xE9es, dont 2 010 personnes\
    \ d\xE9plac\xE9es par les pluies torrentielles, les vents violents et les glissements\
    \ de terrain dans les provinces de Bujumbura Mairie, Bujumbura Rural, Bururi et\
    \ Makamba."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/0b7d77f9-e110-464c-ac63-15375d311e47/download/suivi_des_urgences_24_31_dec_2023_hdx.xlsx
  format: null
  id: resource_0b7d77f9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_24_31_Decembre_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a identifi\xE9 1 030 personnes affect\xE9es (202 m\xE9nages)\
    \ dont 123 personnes d\xE9plac\xE9es (24 m\xE9nages) par les pluies torrentielles\
    \ et les vents violents dans les provinces de Bururi, Cibitoke, Makamba et Muyinga."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/7ee40ecd-f2c9-4ba3-ae38-6bae1cf0053a/download/suivi_des_urgences_2021_17-23122023_public-hdx.xlsx
  format: null
  id: resource_7ee40ecd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_17_23_Decembre_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a identifi\xE9 916 personnes affect\xE9es (185 m\xE9nages)\
    \ dont 716 personnes d\xE9plac\xE9es (136 m\xE9nages) par les pluies torrentielles,\
    \ les inondations et les glissements de terrain dans les provinces de Bujumbura\
    \ Rural et Rutana."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/fe21aefe-7132-443d-b8a8-f0b4c604d68a/download/suivi_des_urgences_10-16_decembre_2023_public-hdx.xlsx
  format: null
  id: resource_fe21aefe
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_10_16_Decembre_2023 Emergency Event Tracking.xlsx.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a identifi\xE9 294 personnes affect\xE9es dont 93 personnes\
    \ d\xE9plac\xE9es par les pluies torrentielles dans les provinces de Rutana et\
    \ Makamba."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/b1b868aa-1646-49f1-8365-178d3ce73945/download/suivi_des_urgences_04-09-decembre-2023_public_hdx.xlsx
  format: null
  id: resource_b1b868aa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_4_9_Decembre_2023 Emergency Event Tracking.xlsx.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a identifi\xE9 4 547 personnes affect\xE9es dont 1286 personnes\
    \ d\xE9plac\xE9es par les pluies torrentielles dans les provinces de Rutana, Rumonge,\
    \ Makamba, Cibtoke et Cankuzo."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/b2e67139-f775-442f-93eb-e45a984ada7c/download/suivi_des_urgences_27_nov_3_dec_2023_public-hdx.xlsx
  format: null
  id: resource_b2e67139
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_27_Novembre_3_Decembre_2023 Emergency Event Tracking.xlsx.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a identifi\xE9 5945 personnes affect\xE9es (1136 m\xE9nages)\
    \ dont 505 personnes d\xE9plac\xE9es (82 m\xE9nages) par les pluies torrentielles\
    \ et les inondations dans les provinces de Kayanza, Rutana, Muramvya, Bujumbura\
    \ Mairie, Gitega, et Cankuzo."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/123a0336-6215-4833-a180-d93cece0527e/download/suivi_des_urgences_20_26_nov_2023_public_hdx.xlsx
  format: null
  id: resource_123a0336
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_20_26_Novembre_2023 Emergency Event Tracking.xlsx.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "En dates du 13 au 19 novembre 2023. La DTM a identifi\xE9 4 944 personnes\
    \ affect\xE9es (942 m\xE9nages) dont 855 personnes d\xE9plac\xE9es (150 m\xE9\
    nages) par les vents violents et les pluies torrentielles dans les provinces de\
    \ Kirundo, Makamba, Rumonge, Rutana et Ruyigi."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/ec61c8df-c991-4555-af84-fe2c003d085d/download/suivi_des_urgences_13_19_nov_2023_public-hdx.xlsx
  format: null
  id: resource_ec61c8df
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_13_19_Novembre_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a identifi\xE9 2 701 personnes affect\xE9es (470 m\xE9nages)\
    \ dont 493 personnes d\xE9plac\xE9es (86 m\xE9nages) par les pluies torrentielles\
    \ et les inondations dans les provinces de Bubanza, Bujumbura Mairie et Rutana."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/f08fd438-cbef-493b-9731-faecdf856f3b/download/suivi_des_urgences_06_12_nov_2023_public-hdx.xlsx
  format: null
  id: resource_f08fd438
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_6_12_Novembre_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a identifi\xE9 91 personnes affect\xE9es dont 91 personnes\
    \ d\xE9plac\xE9es par les vents violents dans les provinces de Rumonge."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/e4799d8a-35e0-4923-8085-618ae9bd66c1/download/suivi_des_urgences_30_oct_5_nov_2023_public_hdx.xlsx
  format: null
  id: resource_e4799d8a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_30_October_5_Novembre_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a identifi\xE9 4,926 personnes affect\xE9es dont 1,493 personnes\
    \ d\xE9plac\xE9es par les vents violents et des pluies torrentielles dans les\
    \ provinces de Mwaro, Kirundo, Bujumbura Mairie, Bururi, Cankuzo et Makamba."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/f3fc73d9-650f-497d-ba29-d21b48afe2fc/download/suivi_des_urgences_23-29_octobre_2023_public_hdx.xlsx
  format: null
  id: resource_f3fc73d9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_23_29_October_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a identifi\xE9 613 personnes affect\xE9es dont 183 personnes\
    \ d\xE9plac\xE9es par les vents violents et des pluies torrentielles dans les\
    \ provinces de Mwaro, Kirundo, Bujumbura Mairie, Bururi, Cankuzo et Makamba."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/729a7774-c3d3-4a49-80a3-4df283b5a36b/download/suivi_des_urgences_15-22oct23_public_hdx.xlsx
  format: null
  id: resource_729a7774
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_15_22_October_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "En dates du 8 au 15 octobre 2023, la DTM a identifi\xE9 10 507 personnes\
    \ affect\xE9es (2 056 m\xE9nages) dont 779 personnes d\xE9plac\xE9es (157 m\xE9\
    nages) par les vents violents, les pluies torrentielles et les inondations dans\
    \ les provinces de Mwaro, Kirundo, Bujumbura Mairie, Bururi, cankuzo et Makamba."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/aa7a07db-75c5-484f-9953-5724d796ee78/download/suivi_des_urgences_8-15_octobre_2023_public.xlsx
  format: null
  id: resource_aa7a07db
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_8_15_October_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a identifi\xE9 2,008 personnes affect\xE9es dont 374 personnes\
    \ d\xE9plac\xE9es par les vents violents et des pluies torrentielles dans les\
    \ provinces de Cibitoke et Kirundo."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/61c09faf-a6e2-48f5-8141-fa7b0ab5fa09/download/suivi_des_urgences_1-7_octobre_2023_public.xlsx
  format: null
  id: resource_61c09faf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_1_7_October_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Du 24 au 30 septembre 2023, la DTM a identifi\xE9 2 878 personnes\
    \ affect\xE9es (519 m\xE9nages) dont 190 personnes d\xE9plac\xE9es (48 m\xE9nages)\
    \ par les pluies torrentielles et les vents violents dans les provinces de Makamba,\
    \ Ngozi et Cibitoke."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/9686511f-2f3e-4d3f-bb0a-ad56e9c95674/download/suivi_des_urgences_23-30_septembre_2023_hdx.xlsx
  format: null
  id: resource_9686511f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_23_30_September_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Du 17 au 23 Septembre La DTM a identifi\xE9 52 personnes affect\xE9\
    es dont 12 personnes d\xE9plac\xE9es par les vents violents dans les province\
    \ de Muyinga."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/05148cb3-efbe-4181-958b-c3adf6b1375e/download/suivi_des_urgences_17-23_septembre_2023_hdx.xlsx
  format: null
  id: resource_05148cb3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_17_23_September_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Du 10 au 16 septembre 2023. La DTM a identifi\xE9 5 152 personnes\
    \ affect\xE9es (1 187 m\xE9nages) dont 1 485 personnes d\xE9plac\xE9es (297 m\xE9\
    nages) par les vents violents, la gr\xEAle et les pluies torrentielles dans les\
    \ provinces de Bujumbura Mairie, Muyinga et Ruyigi."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/3598d9ed-91f3-4b90-84f6-5f4ef63c5578/download/suivi_des_urgences_10-16_septembre_2023_hdx.xlsx
  format: null
  id: resource_3598d9ed
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_10_16_September_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Dates du 3 au 9 septembre 2023, La DTM a identifi\xE9 594 personnes\
    \ affect\xE9es (114 m\xE9nages) dont 144 personnes d\xE9plac\xE9es (27 m\xE9nages)\
    \ par les vents violents dans les provinces de Bubanza et Muyinga."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/c5cacf98-c498-481d-bc16-b84e3bb5996b/download/suivi_des_urgences_3-9_septembre_2023_public_0_hdx.xlsx
  format: null
  id: resource_c5cacf98
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_3_9_September_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Since 2018, natural disasters, in particular torrential rains, floods
    and strong winds that occurred in Burundi affected 588,053 persons, including
    134,351 individuals that have been displaced. During this period, the main affected
    provinces were Bujumbura Rural (131,943 affected persons), Ngozi (111,196 affected
    persons) and Kirundo (98,556 affected persons). Alongside the severe human impact,
    these natural disasters destroyed many houses, infrastructures and crop fields
    in the country.
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/1b491e56-0493-4fae-b0a1-ca3c12c9ad3b/download/burundi-ett-jan-2018-to-may-2023_hdx.xlsx
  format: null
  id: resource_1b491e56
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_Jan_2018_to_May_2023 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM Burundi a le plaisir de vous partager (dans le lien ci-dessus)\
    \ des informations sur les urgences qui se sont produites au Burundi en dates\
    \ du 14 au 20 mai 2023. La DTM a identifi\xE9 978 personnes affect\xE9es (163\
    \ m\xE9nages) dont 69 personnes d\xE9plac\xE9es (10 m\xE9nages) par les pluies\
    \ torrentielles dans la province de Cibitoke."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/c7531657-ba04-4ea6-a367-54d2aaa5e6b5/download/hdx_suivi_des_urgences_14-20_mai_2023.xlsx
  format: null
  id: resource_c7531657
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_14_20_May_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM Burundi a le plaisir de vous partager (dans le lien ci-dessus)\
    \ des informations sur les urgences qui se sont produites au Burundi en dates\
    \ du 7 au 13 mai 2023. La DTM a identifi\xE9 411 personnes affect\xE9es (93 m\xE9\
    nages) dont 350 personnes d\xE9plac\xE9es (75 m\xE9nages) par les pluies torrentielles\
    \ et le glissement de terrain dans les provinces de Bujumbura Rural et Makamba."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/bcef2409-1218-451e-96f1-d6cd886fb0d3/download/public_suivi_des_urgences_7-13_mai_2023_hdx.xlsx
  format: null
  id: resource_bcef2409
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_07_13_May_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM Burundi a le plaisir de vous partager (dans le lien ci-dessus)\
    \ des informations sur les urgences qui se sont produites au Burundi en dates\
    \ du 1 au 6 mai 2023. La DTM a identifi\xE9 43 794 personnes affect\xE9es (9 750\
    \ m\xE9nages) dont 326 personnes d\xE9plac\xE9es (69 m\xE9nages) par les inondations,\
    \ les pluies torrentielles et le glissement de terrain dans les provinces de Bubanza,\
    \ Kirundo et Ruyigi."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/96b3a45d-a5dd-4a62-91b7-b4e99feb545e/download/suivi_des_urgences_1-6_mai_2023_public_hdx.xlsx
  format: null
  id: resource_96b3a45d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_01_06_May_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM Burundi a le plaisir de vous partager (dans le lien ci-dessus)\
    \ des informations sur les urgences qui se sont produites au Burundi en dates\
    \ du 23 au 30 avril 2023. La DTM a identifi\xE9 6 742 personnes affect\xE9es (1\
    \ 304 m\xE9nages) dont 327 personnes d\xE9plac\xE9es (56 m\xE9nages) par les pluies\
    \ torrentielles, les vents violents et la gr\xEAle dans les provinces de Cibitoke,\
    \ Kirundo et Muyinga."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/c519c6b1-17dd-41aa-89be-9195176cbbdd/download/hdx_suivi_des_urgences_23-30_avril_2023.xlsx
  format: null
  id: resource_c519c6b1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_23_30_April__2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Activated on an ad hoc basis, the DTM Emergency Tracking provides early
    field reports at the beginning of a complex crisis, allowing IOM to gather, consolidate
    and disseminate baseline information on displacement and return figures at the
    onset of a newly emerging crisis. The DTM Emergency Tracking relies heavily on
    information provided by RARTs or partners within the humanitarian community about
    an unfolding situation. The Emergency Tracking gathers data through IOM Burundi's
    extended network of key informants, who provide basic information on the new displacement,
    be it of IDPs or returnees, or both, including numbers, location and shelter types.
    While IOM DTM strives to provide best estimates, the Emergency Tracking aims to
    be a quick monitoring tool with real-time data turnover ranging from 24 to 72
    hours following its activation.
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/3f2ee8f1-4a59-42a4-86cf-dfd36e918a19/download/suivi_des_urgences_16-22_april_2023-hdx.xlsx
  format: null
  id: resource_3f2ee8f1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_16_22_April__2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "La DTM a identifi\xE9 19 683 personnes affect\xE9es (3 616 m\xE9nages)\
    \ dont 312 personnes d\xE9plac\xE9es (57 m\xE9nages) par la gr\xEAle, les pluies\
    \ torrentielles et les vents violents dans les provinces de Bubanza, Rumonge,\
    \ Ngozi, Muyinga et Kirundo."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/2fad53b0-32b9-4c49-8312-a1c95f74e076/download/suivi_des_urgences_9-15_avril_2023_hdx.xlsx
  format: null
  id: resource_2fad53b0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_9_15_April__2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi_1_8_April__2023 Emergency Event Tracking.xlsx)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/b100d382-2492-4c46-bdb9-bc121f01016c/download/hdx_suivi_des_urgences_1_au_8_april_2023.xlsx
  format: null
  id: resource_b100d382
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_1_8_April__2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi_26_31_March__2023 Emergency Event Tracking.xlsx)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/70145cd4-7c3b-4718-9e36-cdd6bcfa6a7a/download/hdx_suivi_des_urgences_26-31_march_2023.xlsx
  format: null
  id: resource_70145cd4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_26_31_March__2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi_19_25_March__2023 Emergency Event Tracking.xlsx)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/59ea22fa-00b2-4ea5-95e0-12c287d09c24/download/hdx_suivi_des_urgences_2021_19-25032023.xlsx
  format: null
  id: resource_59ea22fa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_19_25_March__2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi_12_18_March__2023 Emergency Event Tracking.xlsx)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/96045c95-03bf-4b69-a509-776978d616a3/download/hdx_suivi_des_urgences_12-18_march_2023.xlsx
  format: null
  id: resource_96045c95
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_12_18_March__2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi_05_11_March__2023 Emergency Event Tracking.xlsx)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/ecac6db6-a88a-4373-a6a8-8965ba7bfe53/download/hdx-suivi_des_urgences_05-11_march_2023.xlsx
  format: null
  id: resource_ecac6db6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_05_11_March__2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi_26_Feb_04_March__2023 Emergency Event Tracking.xlsx)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/abf337b5-7296-4f01-932f-47fd66b013c1/download/hdx_suivi_des_urgences_26_feb_to_04_march_2023.xlsx
  format: null
  id: resource_abf337b5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_26_Feb_04_March__2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi_19_25_Feb_2023 Emergency Event Tracking.xlsx)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/746b00f6-9834-470f-b9dd-a9a8208c5fe8/download/hdx_suivi_des_urgences_2021_19-25_02_2023.xlsx
  format: null
  id: resource_746b00f6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_19_25_Feb_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DTM Burundi identified 4,699 affected persons and 637 internally displaced
    persons from 6th to 11th february 2023.
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/fe42d641-6950-4706-8a50-398348cae987/download/suivi_des_urgences_06_11_fevrier_2023_public.xlsx
  format: null
  id: resource_fe42d641
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_6_11_Feb_2023 Emergency Event Tracking.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 22nd to 28th january, DTM Burundi has identified 1,948 affected
    persons and 418 internally displaced individuals.
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/ed345aa5-e176-461d-a2cf-9832c0afe05e/download/suivi_des_urgences_22-28-janv_2023_to_be_shared.xlsx
  format: null
  id: resource_ed345aa5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_22_28_Jan_2023 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Activated on an ad hoc basis, the DTM Emergency Tracking provides early
    field reports at the beginning of a complex crisis, allowing IOM to gather, consolidate
    and disseminate baseline information on displacement and return figures at the
    onset of a newly emerging crisis. The DTM Emergency Tracking relies heavily on
    information provided by RARTs or partners within the humanitarian community about
    an unfolding situation. The Emergency Tracking gathers data through IOM Burundi's
    extended network of key informants, who provide basic information on the new displacement,
    be it of IDPs or returnees, or both, including numbers, location and shelter types.
    While IOM DTM strives to provide best estimates, the Emergency Tracking aims to
    be a quick monitoring tool with real-time data turnover ranging from 24 to 72
    hours following its activation.
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/4391c034-20ed-4f2b-a23d-c5e2c1032b81/download/burundi_ett_12_jan_22_jan_2023-2.xlsx
  format: null
  id: resource_4391c034
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_12_22_Jan_2023 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 25 to 31 December, 2022, DTM Burundi has identified 3,625 affected
    peoples including 606 internally displaced persons.
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/d9a2eb31-f512-42fc-a783-78d6219f1ea0/download/suivi_des_urgences_25-31_dec_2022.xlsx
  format: null
  id: resource_d9a2eb31
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 25_31_Dec_2022 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 18 to 24 December, 2022, DTM Burundi has identified 7,540 affected
    peoples including 81 internally displaced persons.
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/07278f08-0f9d-4ded-843c-8507899d2cac/download/suivi_des_urgences_18-24_december_2022.xlsx
  format: null
  id: resource_07278f08
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 18_24_Dec_2022 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 11 to 17 December, 2022, DTM Burundi has identified 8,766 (8,190
    affacted by heavy rains and 576 by strong winds) affected peoples including 531
    (178 displaced due to heavy rains and 576 due strong winds) internally displaced
    persons.
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/0e8150f8-6a9e-4222-aca3-372bea714c28/download/dtm_burundi_suivi_des_urgences_11-17_december_2022.xlsx
  format: null
  id: resource_0e8150f8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 11_17_Dec_2022 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi 04_10_Dec_2022 Emergency Event Tracking)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/7de46b90-22c8-42c7-9138-35bf52247bac/download/dtm_burundi_suivi_des_urgences_4-10dec_2022.xlsx
  format: null
  id: resource_7de46b90
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 04_10_Dec_2022 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From November 28 to December 3, 2022, DTM Burundi has identified 15,659
    peoples affected including 315 internally displaced persons.
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/5c165baf-2502-463b-837f-2708b85e36b1/download/dtm_burundi_ett_suivi_des_urgences_28nov_4dec_2022.xlsx
  format: null
  id: resource_5c165baf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 28_Nov_03_Dec_2022 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From November 21 to 27, 2022, DTM Burundi has identified 212 peoples
    affected by torrential rains, including 207 internally displaced persons in the
    province of Rutana.
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/6bc29321-3d6a-4eb8-8060-7f5ad1b2fd38/download/suivi_des_urgences_21_27nov_2022.xlsx
  format: null
  id: resource_6bc29321
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 21_27 Nov_2022 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From November 07 to 13, 2022, DTM Burundi has identified 88 peoples
    (19 households) affected, including 70 peoples (15 households) displaced by torrential
    rains and strong winds in the provinces of Bururi, Makamba and Ruyigi.
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/4110cd82-1eb7-4b11-ba6d-28210fa6372f/download/suivi_des_urgences_07-13nov_2022.xlsx
  format: null
  id: resource_4110cd82
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 07_13Nov_2022 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi 31Oct_06Nov_2022 Emergency Event Tracking)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/7951f0b2-5082-4a3d-af04-27e4c2edab18/download/suivi_des_urgences_31oct_06nov_2022_to_share.xlsx
  format: null
  id: resource_7951f0b2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 31Oct_06Nov_2022 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi 24-30-oct-2022 Emergency Event Tracking)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/6becc76c-d49d-4d4f-af48-369363a1a874/download/suivi_des_urgences_24-30-oct-2022_to_share.xlsx
  format: null
  id: resource_6becc76c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 24-30-oct-2022 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From October 17 to 23, 2022, DTM Burundi has identified 35,396 peoples
    (7,580 households) affected, including 164 peoples (41 households) displaced by
    hail, torrential rains and strong winds in the provinces of Cibitoke, Kayanza,
    Ngozi, Kirundo and Muyinga.
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/16fe3804-17b5-4e3d-897e-e0846850ad3c/download/hdx_dtm_burundi_suivi_des_urgences_17_au_23-10-2022.xlsx
  format: null
  id: resource_16fe3804
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 17_23Oct_2022 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM Burundi is pleased to share with you information about the
    emergencies that occurred in Burundi on dates from October 3 to 9, 2022. The DTM
    has identified 69 people (11 households) affected, including 54 people (8 households)
    displaced by the strong winds in the province of Rumonge.
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/c4dc71ff-2ef8-4c4b-96ba-9844b4632a4f/download/hdx_suivi_des_urgences_2021_3-9-oct2022_to_share.xlsx
  format: null
  id: resource_c4dc71ff
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 3_9Oct_2022 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi 25Sep_2Oct_2022 Emergency Event Tracking)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/9bdd7108-f4bd-4c5d-bacb-3efbd2d8ea35/download/hdx_suivi_des_urgences_2022-10-04_shared-done.xlsx
  format: null
  id: resource_9bdd7108
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 25Sep_2Oct_2022 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 6,428 peoples (1,281 households) affected, including
    5,363 people (1,055 households) displaced by torrential rains and strong winds
    in the provinces of Cibitoke, Kayanza, Muramvya and Muyinga.
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/936aa04a-c335-4f1c-9159-7709f6338df9/download/hdx_suivi_des_urgences_2021_2022-09-18-25-shared_website.xlsx
  format: null
  id: resource_936aa04a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 18_25Sep_2022 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi 2_8Mar_2020 Emergency Event Tracking)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/2606628f-3670-470f-b63c-cfadb6b62aeb/download/dtm-burundi-2_8mar_2020-emergency-event-tracking.xlsx
  format: null
  id: resource_2606628f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 2_8Mar_2020 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi 24Feb_1Mar_2020 Emergency Event Tracking)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/6f6374f1-b8ae-43cc-a188-7fe4ae343bc1/download/dtm-burundi-24feb_1mar_2020-emergency-event-tracking.xlsx
  format: null
  id: resource_6f6374f1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 24Feb_1Mar_2020 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi 17_23_Feb_2020 Emergency Event Tracking)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/d7bd040a-ce79-4df8-9b93-29738bfb4bd0/download/dtm-burundi-17_23_feb_2020-emergency-event-tracking.xlsx
  format: null
  id: resource_d7bd040a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 17_23_Feb_2020 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi 19_25_Jan_2020 Emergency Event Tracking)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/ec2d22df-1c37-449b-9555-b408bdaa9299/download/dtm-burundi-19_25_jan_2020-emergency-event-tracking.xlsx
  format: null
  id: resource_ec2d22df
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 19_25_Jan_2020 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 2,708 people affected by torrential rains and high winds, distributed
    among 630 households in the provinces of Bubanza, Bujumbura Rural, Muyinga and
    Ruyigi.
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/fdef376e-ac91-414d-8948-af84ef2faa6c/download/dtm-burundi-29sep-05oct-2019-emergency-event-tracking.xlsx
  format: null
  id: resource_fdef376e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 29Sep 05Oct 2019 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi 20_26_Jan_2018 Emergency Event Tracking)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/9536d2c0-b0ac-4313-854f-e539bec8549b/download/dtm-burundi-20_26_jan_2018-emergency-event-tracking.xlsx
  format: null
  id: resource_9536d2c0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 20_26_Jan_2018 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi 30Dec_05_Jan_2018 Emergency Event Tracking)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/a9ec2039-aeef-42d9-8102-0c194a26e048/download/dtm-burundi-30dec_05_jan_2018-emergency-event-tracking.xlsx
  format: null
  id: resource_a9ec2039
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 30Dec_05_Jan_2018 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi 23_29_Dec_2018 Emergency Event Tracking)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/077c0f2b-b13d-43e5-a459-2c42eb4cdd09/download/dtm-burundi-23_29_dec_2018-emergency-event-tracking.xlsx
  format: null
  id: resource_077c0f2b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 23_29_Dec_2018 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement Data - Emergency Event Tracking [IOM DTM] (DTM
    Burundi 16_22_Dec_2018 Emergency Event Tracking)
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/6b1c343c-f77e-4dc5-9307-b5da90a574ce/download/dtm-burundi-16_22_dec_2018-emergency-event-tracking.xlsx
  format: null
  id: resource_6b1c343c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi 16_22_Dec_2018 Emergency Event Tracking
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Dates du 3 au 9 septembre 2023, La DTM a identifi\xE9 594 personnes\
    \ affect\xE9es (114 m\xE9nages) dont 144 personnes d\xE9plac\xE9es (27 m\xE9nages)\
    \ par les vents violents dans les provinces de Bubanza et Muyinga."
  download_url: https://data.humdata.org/dataset/7c50ddcd-3ed2-4a9f-a41f-cacc6c07feb5/resource/c3096b85-c13b-4017-ac57-a2673fa0c9e7/download/suivi_des_urgences_3-9_septembre_2023_public_0_hdx.xlsx
  format: null
  id: resource_c3096b85
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi_3_9_September_2023 Emergency Event Tracking.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bdi_iom_displacementdataemergency_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - BDI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-31'
  start: '2018-01-01'
temporal_resolution: null
title: Burundi Displacement Data - Emergency Event Tracking [IOM DTM]
version: null
vulnerability: null
---
