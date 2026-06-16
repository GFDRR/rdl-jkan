---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/car-baseline-assessment-data-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/car-baseline-assessment-data-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/car-baseline-assessment-data-iom-dtm
dataset_id: rdls_lss-caf_iom_displacementdatabaselinea_2017
description: 'This dataset presents information on internally displaced persons, returnees
  from the Central African Republic who were previously displaced, and returnees from
  other countries. It outlines their distribution by place of origin and period of
  displacement.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/car-baseline-assessment-data-iom-dtm]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IOM DTM conducted repeated baseline assessment surveys (Rounds 5-24)
    across Central African Republic villages and localities using standardized enumeration
    methodology. Data collection involved field teams recording displacement status,
    household and individual counts disaggregated by displacement type (integrated
    locally, relocated), origin location, and triggering cause (conflict, natural
    hazards, mines). Multiple rounds enable temporal tracking of displacement dynamics.
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
- href: https://data.humdata.org/dataset/car-baseline-assessment-data-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from flooding events
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
    description: Internally displaced persons from fire/drought/landslide events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
    description: Internally displaced persons from armed conflict and political crises
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: This dataset presents displacement dynamics at the national level.
    The assessment was carried out in 4,589 localities hosting internally displaced
    persons and or returnees, as well as in 59 displacement sites. Data collection
    took place between 17 October and 27 November 2025 in the country's 19 prefectures,
    plus the capital, Bangui.
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/2bf00ee2-3657-4824-b0ae-8b37a9ac0654/download/dtm_car_baseline_assessment_dec_2025_round_24.xlsx
  format: null
  id: resource_2bf00ee2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 24
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The assessment covered 4,493 localities hosting internally displaced
    persons and returnees, plus 75 displacement sites. Data collection ran from 2
    December 2024 to 31 January 2025 across the 19 prefectures and the capital, Bangui.
    In this round, DTM identified 422,616 internally displaced persons, 2,334,310
    internal returnees, and 547,653 returnees from abroad.
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/212517d0-411c-4442-b50a-2d48965ad724/download/dtm_car_baseline_assessment_round_23_jan_2025_hdx.xlsx
  format: null
  id: resource_212517d0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 23
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset offers an overview of national displacement dynamics.
    Data was collected between August 1 and September 9, 2024, across 16 prefectures
    and the capital, Bangui, covering 4,521 localities hosting IDPs and/or returnees,
    as well as 69 displacement sites. During this round 22, a total of 431,966 IDPs,
    2,309,365 internal returnees, and 539,800 returnees from abroad were identified.
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/c8c588c9-dc62-43fc-84fc-173e864857bf/download/dtm_car_baseline_assessment_round_22_aug_2024_hdx.xlsx
  format: null
  id: resource_c8c588c9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 22
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset provides an overview of national displacement dynamics.
    Data was collected between April 1 and May 9, 2024, across 16 prefectures and
    the capital, Bangui. During this round 21, a total of 446,614 IDPs, 2,256,970
    internal returnees, and 531,919 returnees from abroad were identified.
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/414142a8-9f78-4f8d-af4f-4d3eb2f43785/download/dtm_car_b2f_villages_round_21_hdx.xlsx
  format: null
  id: resource_414142a8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 21
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "L'\xE9valuation a \xE9t\xE9 r\xE9alis\xE9e dans 4 410 localit\xE9\
    s de pr\xE9sence des PDI et / ou retourn\xE9s et 77 sites de d\xE9placement. La\
    \ collecte de donn\xE9es s'est tenue entre le 02 d\xE9cembre 2023 et le 09 janvier\
    \ 2024 dans les 16 pr\xE9fectures du pays en plus de la capitale Bangui."
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/89301207-3660-4807-a989-a0fd8a0437f4/download/dtm_car_dataset_rd20_february-2024-hdx.xlsx
  format: null
  id: resource_89301207
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 20
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset presents national travel dynamics. The assessment was
    conducted at 4,224 locations of IDP occurrence and/or return and 79 displacement
    sites. Data collection took place between August 1 and September 8, 2023 in the
    country's 16 prefectures in addition to the capital Bangui.
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/e1d706aa-f2cc-43b0-80f1-60280945371c/download/dtm_car_round-19_data_aout-2023_publication.xlsx
  format: null
  id: resource_e1d706aa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 19
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The round 18 assessment was carried out in 4,200 localities of presence
    of IDPs and/or returnees and 78 displacement sites. The data collection took place
    between May 01 and June 08, 2023 in the 16 prefectures of the country in addition
    to the capital Bangui. During this round, the DTMa team identified 452,761 IDPs
    and a total of 2,566,904 returnees, including 2,063,855 internal returnees and
    503,019 returnees from other countries.
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/de09da4e-f8c6-4433-a1e3-d9f4888f07ca/download/dtm_central_african_republic_mt_baseline_assessment_round_18_may_2023.xlsx
  format: null
  id: resource_de09da4e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 18
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A baseline assessment is a sub-component of mobility tracking. It aims
    to collect data on IDP, migrant or returnee population presence in a defined administrative
    area of the country.
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/49583873-d2db-4e78-b4e0-eaad9067a3dc/download/dtm_hdx__car_rnd-17_data-and-analysis_displacement.xlsx
  format: null
  id: resource_49583873
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 17
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A baseline assessment is a sub-component of mobility tracking. It aims
    to collect data on IDP, migrant or returnee population presence in a defined administrative
    area of the country.
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/398a783a-6f5f-4f01-96e4-b4a779fa2542/download/hdx_dtm_round-16_b2f_database_external.xlsx
  format: null
  id: resource_398a783a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 16
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Depuis plusieurs ann\xE9es, la R\xE9publique centrafricaine (RCA)\
    \ est affect\xE9e par des crises politiques, s\xE9curitaires et humanitaires li\xE9\
    es aux conflits arm\xE9s, aux conflits intercommunautaires ou provoqu\xE9es par\
    \ des tensions entre agriculteurs et \xE9leveurs dans certaines zones. La situation\
    \ s\xE9curitaire est rest\xE9e volatile tout au long du premier semestre 2022\
    \ marqu\xE9e par des op\xE9rations militaires et des affrontements opposant les\
    \ Forces Arm\xE9es Centrafricaine (FACA) appuy\xE9es par leurs alli\xE9s aux groupes\
    \ arm\xE9s luttant pour le contr\xF4le des territoires. Ces affrontements et exactions\
    \ perp\xE9tr\xE9es par des \xE9l\xE9ments arm\xE9s continuent d'occasionner des\
    \ d\xE9placements pr\xE9ventifs ou \xE0 la suite d'incidents s\xE9curitaires dans\
    \ toutes les zones du pays. De surcro\xEEt, les pluies diluviennes causant des\
    \ inondations pendant la p\xE9riode pr\xE9-hivernale et hivernale (de juin \xE0\
    \ novembre) accroissent la vuln\xE9rabilit\xE9 des populations en engendrant le\
    \ d\xE9placement de milliers de personnes."
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/f28cc1bd-6a4f-4b5b-ac03-970ed07c9ed7/download/hdx_dtm-rca_rnd-15_data_june-2022.xlsx
  format: null
  id: resource_f28cc1bd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 15
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Depuis plusieurs ann\xE9es, la R\xE9publique centrafricaine (RCA)\
    \ est touch\xE9e par des crises politiques, s\xE9curitaires et humanitaires li\xE9\
    es aux conflits arm\xE9s, aux conflits intercommunautaires ou provoqu\xE9es par\
    \ des conflits entre agriculteurs et \xE9leveurs dans certaines zones. En r\xE9\
    ponse aux crises complexes en RCA, l'Organisation Internationale pour les Migrations\
    \ (OIM) d\xE9ploie, depuis d\xE9cembre 2013, la Matrice de Suivi des D\xE9placements\
    \ (Displacement Tracking Matrix, DTM), un outil qui collecte des donn\xE9es sur\
    \ les tendances de d\xE9placement ainsi que les besoins humanitaires multisectoriels\
    \ des personnes affect\xE9es par les crises. Ce jeu de donn\xE9es pr\xE9sente\
    \ la situation de d\xE9placement dans les localit\xE9s et sites d'accueil des\
    \ d\xE9plac\xE9s internes et retourn\xE9s. La collecte de donn\xE9es a \xE9t\xE9\
    \ r\xE9alis\xE9e aupr\xE8s de 7 287 informateurs cl\xE9s entre le 15 d\xE9cembre\
    \ 2021 et le 27 janvier 2022 dans 11 pr\xE9fectures en plus de la capitale Bangui\
    \ : Bamingui-Bangoran, Haute-Kotto, Haut-Mbomou, Nana-Gribizi, Basse-Kotto, Nana-Mambere,\
    \ Ombella-Mpoko, Ouaka, Mbomou, Ouham-Pende et Ouham (collecte r\xE9alis\xE9e\
    \ uniquement dans les sites et non les localit\xE9s dans l'Ouham)."
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/0fb63289-fe04-4b8d-baa3-d416822564b1/download/hdx-dtm-car-dataset-deplacement-round-14.xlsx
  format: null
  id: resource_0fb63289
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 14
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: During this thirteenth round of movement monitoring, the DTM listed
    1,798,001 mobile individuals as of end of September 2021, including 393,854 IDPs
    (81,219 households) and 1,404,147 returnees including 1,070,749 internal returnees
    (215,602 households) and 333,398 returnees from abroad (67,313 households). Of
    the IDP households listed, 66 percent live within host communities, 31 percent
    of official sites and 3 percent on unofficial sites.
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/0554df81-920a-4769-9fbe-e85a3cba5a67/download/dtm_round-13_car_hdx.xlsx
  format: null
  id: resource_0554df81
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 13
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: Displacement Data - Baseline Assessment
    [IOM DTM] (DTM CAR Baseline Assessment Round 12)'
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/7e58ed6e-39f9-4c8f-88d5-2401062f5ff2/download/hdx_dtm_car_baseline_assessment_donnees_localites_round_12_juin_2021.xlsx
  format: null
  id: resource_7e58ed6e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 12
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: Displacement Data - Baseline Assessment
    [IOM DTM] (DTM CAR Baseline Assessment Round 11)'
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/7711b5da-0560-4c48-ac5d-0a6da0c7b253/download/dtm-car-baseline-assessment-round-11.xlsx
  format: null
  id: resource_7711b5da
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 11
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: Displacement Data - Baseline Assessment
    [IOM DTM] (DTM CAR Baseline Assessment Round 10)'
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/1b404b9a-40ab-4f6f-b7d2-eaf0bf0493c4/download/dtm-car-baseline-assessment-round-10.xlsx
  format: null
  id: resource_1b404b9a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 10
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This Round 9 DTM assessment identified a total of 1,492,273 individuals.
    These figures include 528,140 IDPs, 680,950 internal returnees and 283,183 returnees
    from abroad. Following the previous DTM round (July 2019), the key results presented
    in this report highlight the continuous increase in internal returns (+ 12% compared
    to round 8 in July 2019) and cross-border returns (+ 8% ). Finally, a decrease
    in internal displacements is observed (-2%).
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/3f216e0e-220c-4286-9fd6-fb60e2ba36ac/download/dtm-car-baseline-assessment-round-9.xlsx
  format: null
  id: resource_3f216e0e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 9
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Round 8 of the DTM assessments, carried out between May 30 and July
    15 in 1 426 localities of the nine prefectures covered. DTM identified a total
    of 1,401,255 individuals, including 537,285 IDPs, 600,473 internal returnees and
    263,497 returned from abroad.
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/3b65fc4e-d467-454a-a848-730b2fa556ed/download/dtm-car-baseline-assessment-round-8.xlsx
  format: null
  id: resource_3b65fc4e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 8
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: There are around 464,000 IDPs in CAR. Between Round 6 and Round 7,
    the number of IDPs has decreased by 20 per cent. In parallel, the number of returnees
    (former IDPs) has increased by 21 per cent. As a result, some sitesin the prefecture
    of Ouaka were closed.
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/a0410fbf-92b6-4087-8a2c-7d3d2244e2a4/download/dtm-car-baseline-assessment-round-7.xlsx
  format: null
  id: resource_a0410fbf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 7
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'In round 6 the DTM identified a total displaced population of 1,074,983
    individuals: 580,692 Internally Displaced Persons (IDPs), 375,684 returnees (former
    IDPs) and 118,607 returnees from other countries. 25% of internal displacements
    are due to intercommunity tensions, against 68% related to armed conflicts and
    5% as a preventive measure. The displaced population is 49% male and 51% female.'
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/79642483-5781-4ee1-a1a3-816bfb796a37/download/dtm-car-baseline-assessment-round-6.xlsx
  format: null
  id: resource_79642483
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 6
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Information collected in 9 prefectures (Bamingui-Bangoran, Bangui,\
    \ Lower Kotto, Upper Kotto, Haut-Mbomou, Mbomou, Nana-Gribizi, Ouaka, and Ouham\
    \ Pend\xE9). The DTM identified a total displaced population of 965,364 individuals:\
    \ 547,814 Internally Displaced Persons (IDPs), 309,826 returned (former IDPs)\
    \ and 107,724 returned from other countries. 26% of internal displacements are\
    \ due to inter-community tensions, compared to 67% linked to armed conflicts and\
    \ 6% as a preventive measure. The displaced population is 49% male and 51% female."
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/2a9f4e13-b758-43fa-bcf3-d3619b72a1e9/download/dtm-car-baseline-assessment-round-5.xlsx
  format: null
  id: resource_2a9f4e13
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 5
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 557,723 IDPs and 117,888 households. 59% of the displaced population
    Returned CAR i.e. 301,603 individuals and 32% Returned from other countries. The
    average size of a displaced household is 8 people. 98% of households IDPs have
    children and the average number of children per household is 5.5. The displaced
    population is 48% male and 52% female. 67% of the population is composed of minors
    between 0 and 18 years old. People over 60 represent 6% of the displaced.
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/84644264-d4a6-4fab-b7d6-ce6d403cf37c/download/dtm-car-baseline-assessment-round-4.xlsx
  format: null
  id: resource_84644264
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 4
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This is a DTM CAR baseline assessment dataset. Data have been collected
    from 23rd March to 6th April 2018 in six admin1 with a partial coverage of some
    admin2 for insecurity reasons.
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/5744be67-838c-4ae4-a496-dbcc8f580391/download/dtm-car-baseline-assessment-round-3.xlsx
  format: null
  id: resource_5744be67
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 3
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: Displacement Data - Baseline Assessment
    [IOM DTM] (DTM CAR Baseline Assessment Round 2)'
  download_url: https://data.humdata.org/dataset/5fa6eebf-2a6d-4aca-bb4e-fb625cb3b44d/resource/a000e81d-eea9-4fb0-8fcd-da548b5eb057/download/dtm-car-baseline-assessment-round-2.xlsx
  format: null
  id: resource_a000e81d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Baseline Assessment Round 2
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-caf_iom_displacementdatabaselinea_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - CAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-11-27'
  start: '2017-11-30'
temporal_resolution: null
title: 'Central African Republic: Displacement Data - Baseline Assessment [IOM DTM]'
version: null
vulnerability: null
---
