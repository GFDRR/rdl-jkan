---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/cameroon-baseline-assessment-data-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/cameroon-baseline-assessment-data-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/cameroon-baseline-assessment-data-iom-dtm
dataset_id: rdls_lss-cmr_iom_displacementidpsreturnees_2015
description: 'The dataset contains IDPs, Returnees and Refugees at sub national level
  with information on IDPs in camps and host communities. IOM set up and rolled out
  the first round of the DTM in November 2015 with the objective of providing regular,
  accurate and updated information on displaced populations within the Far North region
  of Cameroon to better support the response of the Government of Cameroon and the
  humanitarian community.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cameroon-baseline-assessment-data-iom-dtm]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IOM DTM conducted repeated baseline assessments (29 rounds) of displaced
    populations in Far North Cameroon starting November 2015, collecting household
    and individual counts of IDPs in camps and host communities, refugees, and returnees
    at village and administrative levels using standardized DTM methodology to support
    government and humanitarian response.
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
- href: https://data.humdata.org/dataset/cameroon-baseline-assessment-data-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from conflict and insecurity in Far
      North Cameroon
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
    description: Refugee populations from regional displacement crises
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  - asset_category: population
    asset_dimension: population
    description: Returnee populations resettling in Far North Cameroon
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
  description: "This dataset provides information on displacement in 1,423 target\
    \ locations (including 1,237 villages and 186 spontaneous sites) hosting internally\
    \ displaced persons (IDPs), returnees, and out-of-camp refugees. Data collection\
    \ was carried out from 28 May to 23 June 2025 across six departments (Diamar\xE9\
    , Logone-Et-Chari, Mayo-Danay, Mayo-Kani, Mayo-Sava, and Mayo-Tsanaga) in the\
    \ Far North region."
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/2cafba43-1da0-493b-b05b-15972044ec21/download/iom_dtm_cmr_mt_baseline_round_29_june_2025_hdx.xlsx
  format: null
  id: resource_2cafba43
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 29
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This dataset provides information on the displacement situation in\
    \ 1,316 targeted locations, including 1,160 villages and 156 spontaneous sites\
    \ hosting internally displaced persons (IDPs), returnees, and out-of-camp refugees.\
    \ Data collection was carried out with 3,689 key informants, and 18 focus group\
    \ discussions were conducted between 19 and 30 June 2024 across the six departments\
    \ (Diamar\xE9, Logone-Et-Chari, Mayo-Danay, Mayo-Kani, Mayo-Sava, and Mayo-Tsanaga)\
    \ of the Far North region."
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/e8ce6f9e-80d7-4662-9edb-328c892abd0c/download/iom_dtm_cameroon_baseline_assessment_july_2024_round_28_hdx.xlsx
  format: null
  id: resource_e8ce6f9e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 28
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collection for round 27 was conducted from 18 to 29 August 2023
    through 3,715 key informants, accross 1,283 localities. During this round, 700,766
    internally displaced individuals were identified, including 453,661 IDPs, 198,940
    Returnees, and 48,165 Out-of-camp refugees
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/e1953bbd-432e-4449-b417-dae7487663d0/download/iom_dtm_cmr_round_27_mobility_tracking_baseline_sept.2023_hdx.xlsx
  format: null
  id: resource_e1953bbd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 27
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Data collection for round 26 was conducted from 8 to 20 February 2023\
    \ through 3,715 key informants, in 6 departments (Diamar\xE9, Logone Et Chari,\
    \ Mayo Danay, Mayo Kani, Mayo Sava and Mayo Tsanaga) ) of the Far North region.\
    \ During this round, 680,512 mobile individuals were identified, including 427,833\
    \ IDPs, 203,166 Returnees, and 49,513 Out-of-camp refugees"
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/313883e3-1a2c-4537-b297-044c18514fe5/download/iom_dtm_cameroon_round_26_mobility_tracking_baseline_feb_2023.xlsx
  format: null
  id: resource_313883e3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 26
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'During this twenty-fifth cycle of monitoring of displacements (Round
    25), the DTM identified 573,184 mobile individuals in August 2022 who left as
    follows: 385,372 (67%) internally displaced persons including 138,152 (24%) Returned
    and 49,660 (9%) Out-of-camp refugees.'
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/c3b10e91-d752-49a1-8053-bbf0e434a801/download/hdx_iom_dtm_cmr_round_25_mobility_tracking_baseline_sept_2022_20220922.xlsx
  format: null
  id: resource_c3b10e91
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 25
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: During this round 24, an estimated total of more than 558,000 individuals
    was identified, including 378,000 IDPs, including 50,000 refugees out of camp
    and 131,000 returnees. The number of IDPs has increased by 6 percent, the number
    of refugees out of camp has decreased by 5 percent and the number of returnees
    has decreased by 3 percent since the last round.
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/2f182620-ad2e-4d5f-943a-55a6a3a7a323/download/dtm-cameroon-baseline-assessment-round-24.xlsx
  format: null
  id: resource_2f182620
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 24
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset gives an overview of the situation in the Far North region
    of Cameroon, where insecurity linked to the violence of armed extremist groups
    and, to a lesser extent, climatic phenomena and seasonal rains, have given rise
    to significant population movements. The information presented in this dataset
    was collected from displaced people with the agreement and support of local authorities,
    between July 7 and 18, 2021. In round 23 of the DTM, an estimated total of nearly
    550,000 individuals was identified, including 357,631 IDPs, including 51,997 refugees
    out of camp and 135,257 returnees. The mobile population in the region has increased
    by 6 percent compared to the previous round (March 2021). The number of IDPs has
    increased by 5 percent, the number of refugees out of camp has increased by 6
    percent and the number of returnees has increased by 9 percent since the last
    round.
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/39e76895-b94e-4ade-ba46-10e3cf3137b2/download/iom_dtm_cmr_round_23_mobility_tracking_baseline_aug_2021.xlsx
  format: null
  id: resource_39e76895
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 23
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Round 22 data collection took place between 12 March and 31 March 2021.
    During this round, a total of 514,747 individuals were identified, 341,535 IDPs
    (55,912 households), 48,902 out-of-camp refugees (8,111 households) and 124,310
    returnees (18,563 households).
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/4219ee77-664c-42ba-a98c-d1ee4135dda1/download/dtm-cameroon-baseline-assessment-round-22_hdx.xlsx
  format: null
  id: resource_4219ee77
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 22
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The file has IDPs, Refugees and Returnees information along with information
    on COVID-19. There is are summary and analysis sheets in the file for better understanding.
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/4f3cb8ab-ea62-4736-a208-0a433349e574/download/dtm-cameroon-baseline-assessment-round-21.xlsx
  format: null
  id: resource_4f3cb8ab
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 21
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data was collected between 25 November and 6 December 2019. The displaced
    population is estimated at 461,664 individuals (297,380 IDPs, 47,305 out of camp
    refugees and 116,979 returnees). 931 locations were assessed including 68 new
    villages.
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/a013e7e4-649f-4eab-99be-69d0ad22a608/download/dtm-cameroon-baseline-assessment-round-20.xlsx
  format: null
  id: resource_a013e7e4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 20
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data was collected between 12-25 August 2019. The displaced population
    is estimated at 428,289 individuals (270,870 IDPs, 46,845 out of camp refugees
    and 110,574 returnees). 863 villages were evaluated, including 10 new villages.
    50.2% of the displaced population were male and 49.8% were female. 62% were under
    18 years old. 49% of IDPs lived with host families, 27% lived in spontaneous sites,
    15% lived in rental homes, 7% lived in new homes and 2 per cent live in collective
    centers. The priority needs of those displaced were drinking water, food and health
    care.
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/45b56ed2-6efc-4dcf-b7d2-d78b521e6ee4/download/dtm-cameroon-baseline-assessment-round-19.xlsx
  format: null
  id: resource_45b56ed2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 19
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collected on the displacement situation in the Far North Region
    of Cameroon between 28 March and 8 April 2019. The displaced population is estimated
    at 423,835 individuals, 262,831 IDPs, 50,981 out of camp refugees and 110,023
    returnees.
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/669c349e-2545-4438-8a18-5e8cd4b39d5e/download/dtm-cameroon-baseline-assessment-round-18.xlsx
  format: null
  id: resource_669c349e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 18
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collected in the Far North Region of Cameroon between 1-13th of
    February 2019. The displaced population is estimated at 442,683 individuals (253,813
    IDPs, 79,787 out of camp refugees and 109,083 returnees). 844 villages were evaluated
    including 9 new villages. 66 uninhabited villages were identified. 94% of the
    target population is displaced due to armed conflict in the Region and 6% is displaced
    due to flooding and other climatic factors.
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/9b60bd95-ad82-4b37-b3f9-61c71a2289e0/download/dtm-cameroon-baseline-assessment-round-17.xlsx
  format: null
  id: resource_9b60bd95
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 17
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The displaced population in Cameroon's Far North Region is estimated
    at 392,027 individuals (245,725 IDPs, 40,396 out of camp refugees and 105,906
    returnees).
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/74949680-d339-43eb-83ff-5aa840fe0fd7/download/dtm-cameroon-baseline-assessment-round-16.xlsx
  format: null
  id: resource_74949680
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 16
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The displaced population in Cameroon's Far North Region is estimated
    at 387,035 individuals (244,347 IDPs, 41,763 out of camp refugees and 100,925
    returnees). 806 villages were evaluated including 4 new villages. 66 uninhabited
    villages were identified.
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/b450d6c7-c43e-4614-a146-1f73d0af6e22/download/dtm-cameroon-baseline-assessment-round-15.xlsx
  format: null
  id: resource_b450d6c7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 15
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data was collected between 13-26 June 2018. The displaced population
    is estimated at 359,222 individuals (2227,581 IDPs, 39,403 out of camp refugees
    and 92,238 returnees). 786 villages were evaluated including 27 new villages.
    68 uninhabited villages were identified. 93% of the target population is displaced
    due to armed conflict in the Region and 7% is displaced due to flooding and other
    climatic factors.
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/f9869d2d-553e-4e20-a62f-0e461d195784/download/dtm-cameroon-baseline-assessment-round-14.xlsx
  format: null
  id: resource_f9869d2d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 14
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'The displaced population is estimated at 352,921 individuals: 238,099
    internally displaced persons (IDPs), 31,681 non-camp refugees and 83,141 returned.
    92% of displaced populations are displaced by armed conflict in the region. 7%
    of displacements are caused by floods, drought and other climatic factors. 1%
    of trips are caused by other unspecified reasons. Data collected from 12 to 24th
    of April'
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/69c1b3e2-9875-4c5f-96b8-25812e1c75fd/download/dtm-cameroon-baseline-assessment-round-13.xlsx
  format: null
  id: resource_69c1b3e2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 13
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The displaced population is estimated 342,416 individuals (241,030
    IDPs, 31,656 out of camp refugees and 69,730 returnees). 747 villages were evaluated
    including 4 new villages. 69 uninhabited villages were identified. 91% of the
    target population is displaced due to armed conflict in the region and 9% is displaced
    due to flooding and other climatic factors. 51% of the displaced population is
    male and 49% is female. 65% are under 18 years old, while 3% are 60 years old
    or older. 45% of those displaced live with host families, 15% live in rented houses,
    22% live in spontaneous sites, 14% returned to their original dwelling, and one
    per cent live in the open air without shelter.
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/560600db-6155-4ddf-a8ed-bbd4b753509b/download/dtm-cameroon-baseline-assessment-round-12.xlsx
  format: null
  id: resource_560600db
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 12
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: he displaced population is estimated at 335,016 individuals (241,987
    IDPs,29,337 out of camp refugees and 63,692 returnees). 743 villages were evaluated
    including 14 new villages. 60 uninhabited villages were identified. 92% of the
    target population is displaced due to armed conflict in the Region and 8% is displaced
    due to flooding and other climatic factors. 47% of those displaced live with host
    families, 16% rent houses, 23% live in spontaneous sites, and less than one per
    cent live in the open air without shelter.
  download_url: https://displacement.iom.int/system/tdf/datasets/CMR_Baseline_Analysis_Rd11_v4.xlsx?file=1&type=node&id=2555
  format: null
  id: resource_7b1e0afc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 11
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The displaced population is estimated at 328,785 individuals (237,967
    IDPs, 29,728 unregistered refugees and 61,090 returnees). 726 villages were evaluated
    including 3 new villages. 56 uninhabited villages were identified. 92% of the
    target population is displaced due to armed conflict in the Region. 46% of those
    displaced live with host families, 16% rent houses, 24% live in spontaneous sites,
    14% returned to their original dwellings, 1% live in collective centers and 1%
    live in the open air without shelter.
  download_url: https://displacement.iom.int/system/tdf/datasets/Copy%20of%20Round%2010%20Baseline.xlsx?file=1&type=node&id=2151
  format: null
  id: resource_af49bda2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 10
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cameroon Displacement - [IDPs, Returnees, Refugees] - Baseline Assessment
    [IOM DTM] (DTM Cameroon Baseline Assessment Round 9)
  download_url: https://data.humdata.org/dataset/140a45e9-6563-47e7-89b1-9109d89a2211/resource/371ef58f-c6f7-4a97-8e4c-1afa7cd20edc/download/dtm-cameroon-baseline-assessment-round-12.xlsx
  format: null
  id: resource_371ef58f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 9
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Identified an estimated 318,929 individuals comprising 228,443 IDPs,
    32,459 unregistered refugees and 58,027 returnees. 674 villages were surveyed
    including 56 new villages. 96% of the assessed population were displaced due to
    armed conflict in the region. 51% of the displaced population are men and boys,
    while 49% are women and girls. 53% of the population are children from 0 to 12
    years of age. 52% of displaced households live with host families, 24% occupy
    rental space, 17% live in spontaneous sites, 4% live in collective centres and
    2% live in exposed, open air environments.
  download_url: https://displacement.iom.int/system/tdf/datasets/05_IOM%20DTM%20Dataset%20Cameroon_Round8_2017.xlsx?file=1&type=node&id=1529
  format: null
  id: resource_1f84ea37
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 8
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 223,642 IDPs (39,002 households), 30,593 unregistered refugees (4,987
    households) and 43,435 returnees (7,347 households).
  download_url: https://displacement.iom.int/system/tdf/datasets/05_IOM%20DTM%20Dataset%20Cameroon_Round7_2015.xlsx?file=1&type=node&id=1528
  format: null
  id: resource_21d7fc5e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 7
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cameroon Displacement - [IDPs, Returnees, Refugees] - Baseline Assessment
    [IOM DTM] (DTM Cameroon Baseline Assessment Round 6)
  download_url: https://displacement.iom.int/system/tdf/datasets/05_IOM%20DTM%20Dataset%20Cameroon_Round6_201701.xlsx?file=1&type=node&id=1526
  format: null
  id: resource_9b83b24f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 6
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cameroon Displacement - [IDPs, Returnees, Refugees] - Baseline Assessment
    [IOM DTM] (DTM Cameroon Baseline Assessment Round 5)
  download_url: https://displacement.iom.int/system/tdf/datasets/Cameroon_baseline_round5.xlsx?file=1&type=node&id=633
  format: null
  id: resource_ab84a97b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 5
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cameroon Displacement - [IDPs, Returnees, Refugees] - Baseline Assessment
    [IOM DTM] (DTM Cameroon Baseline Assessment Round 4)
  download_url: https://displacement.iom.int/system/tdf/datasets/Cameroon_baselie_round4.xlsx?file=1&type=node&id=603
  format: null
  id: resource_681c3af3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 4
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cameroon Displacement - [IDPs, Returnees, Refugees] - Baseline Assessment
    [IOM DTM] (DTM Cameroon Baseline Assessment Round 3)
  download_url: https://displacement.iom.int/system/tdf/datasets/Cameroon_baseline_round3.xlsx?file=1&type=node&id=596
  format: null
  id: resource_53b77775
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 3
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cameroon Displacement - [IDPs, Returnees, Refugees] - Baseline Assessment
    [IOM DTM] (DTM Cameroon Baseline Assessment Round 2)
  download_url: https://displacement.iom.int/system/tdf/datasets/Cameroon_baseline_round2.xlsx?file=1&type=node&id=635
  format: null
  id: resource_eda4d6a2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 2
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cameroon Displacement - [IDPs, Returnees, Refugees] - Baseline Assessment
    [IOM DTM] (DTM Cameroon Baseline Assessment Round 1)
  download_url: https://displacement.iom.int/system/tdf/datasets/r1%20Cameroon_with%20analysis.xlsx?file=1&type=node&id=1525
  format: null
  id: resource_60d274e8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Cameroon Baseline Assessment Round 1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cmr_iom_displacementidpsreturnees_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - CMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-06-23'
  start: '2015-11-10'
temporal_resolution: null
title: Cameroon Displacement - [IDPs, Returnees, Refugees] - Baseline Assessment [IOM
  DTM]
version: null
vulnerability: null
---
