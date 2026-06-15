---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/burundi-baseline-assessment-data-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/burundi-baseline-assessment-data-iom-dtm
dataset_id: rdls_lss-bdi_iom_displacementidpsbaselinea_2016
description: 'The dataset contains IDPs individuals and households at admin2 level.
  IOM has been developing a Displacement Tracking Matrix (DTM) since May 2015 aimed
  at effectively monitoring and evaluating the flows of Burundian IDPs and providing
  accurate information on the current IDP situation. The DTM in Burundi has been successfully
  used in 2014, upon the request of the humanitarian community and the GoB when some
  areas of Bujumbura were flooded, which caused displacement. This tool allowed registering
  IDPs in four IDP sites and in host families in four locations and identifying their
  humanitarian needs. The dataset includes returnees from abroad who are still displaced
  in the country. They are categorized as IDPs due to their continued displacement
  within the country.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/burundi-baseline-assessment-data-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM collects displacement data through key informant interviews
    at colline (sub-commune) level across Burundi, recording IDP household and individual
    counts disaggregated by demographics and displacement cause (natural disasters,
    socio-political, other). Data is compiled into baseline assessment rounds tracking
    displacement flows and population characteristics over time.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/burundi-baseline-assessment-data-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from flood events and other natural
      disasters
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
    description: Population affected by natural disasters including floods
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
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://displacement.iom.int/sites/default/files/public/Methodological%20Framework%20used%20in%20DTM%20Operations%20for%20Quantifying%20Displacement%20and%20Mobility.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (In round
    78, 89,114 IDPs and 18,024 displaced households were assessed.)
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/5aab20c1-38ad-40a3-b857-ce57ce93738c/download/burundi_baseline_july-2025_publish.xlsx
  format: null
  id: resource_5aab20c1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 78
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (In round
    77, 92,227 IDPs and 19,013 displaced households were assessed.)
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/7ae6f90b-1413-4147-8fa4-d6718a442476/download/dtm_burundi_fiche_colline_baseline_publish_hdx.xlsx
  format: null
  id: resource_7ae6f90b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 77
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (In round
    76, 86,159 IDPs and 18,055 displaced households were assessed.)
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/adb7269d-e074-4262-a271-adf9da887c04/download/dtm_burundi_baseline_august_2024_publish_hdx.xlsx
  format: null
  id: resource_adb7269d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 76
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (In round
    75, 102,824 IDPs and 21,979 displaced households were assessed.)
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/e8cc9d22-1627-40d2-937b-7d01c1d06633/download/dtm_burundi_baseline_may_2024_to_be_shared_hdx.xlsx
  format: null
  id: resource_e8cc9d22
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 75
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'IOM''s Displacement Tracking Matrix is a comprehensive system to analyse
    and disseminate information to better understand the movements and needs of Internally
    Displaced Persons (IDPs) in Burundi. The baseline assessment aims at providing
    information on the stock (presence) by colline of IDPs which are categorized into
    two groups: Internally Displaced Persons (IDPs) including IDPs who returned to
    their colline of origin but not their home and returnees who became IDPs. The
    baseline assessment also collects information on the cause of displacement and
    the type of shelter hosting IDPs. Data collection is conducted four times per
    year by trained Burundian Red Cross volunteers operating at all administrative
    levels: provinces, communes and collines. In Round 74, 79,917 IDPs and 17,008
    displaced households were assessed.'
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/80f1cedc-13a2-4428-a8e0-72782fa4a8ac/download/dtm_burundi_baseline_february_2024_to_be_shared_publish.xlsx
  format: null
  id: resource_80f1cedc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 74
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 73,931 IDPs and 17,151 displaced households were identified in July
    2023 in Burundi.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/c50a1711-f5f8-471b-9887-85d396f19ddd/download/dtm_burundi_baseline_juillet_2023_to-be-shared.xlsx
  format: null
  id: resource_c50a1711
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 73
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'The baseline assessment aims at providing information on the stock
    (presence) by colline of IDPs which are categorized into two groups: Internally
    Displaced Persons (IDPs) including IDPs who returned to their colline of origin
    but not their home and returnees who became IDPs. The baseline assessment also
    collects information on the cause of displacement and the type of shelter hosting
    IDPs. Data collection is conducted four times per year by trained Burundian Red
    Cross volunteers operating at all administrative levels: provinces, communes and
    collines. From 2 May to 19 May 2023, DTM Burundi has identified 76,987 displaced
    individuals including 69,535 internal displaced persons and 7,452 * returnees
    from abroad who remain displaced in country accross 1,324 collines (administrative
    boundaries level 3). Internally Displaced Persons (IDPs): are Burundian nationals
    who have been forced to flee or forced to leave their home or their usual place
    of residence, in particular as a result of armed conflict, situations of violence
    widespread, human rights violations or natural or man-made disasters or to avoid
    their effects, and which have not crossed the internationally recognized borders
    of a State. For the purpose of DTM, only IDPs displaced since 2013 or later are
    considered IDPs. *Returnees who became IDPs: Burundian nationals who had been
    displaced outside the country and have since returned (spontaneously or assisted)
    to Burundi but continue being in displacement (because their houses were destroyed
    or for other reasons).'
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/5379ed75-c7bb-4c1b-bb14-02443f7c74a2/download/dtm_burundi_baseline_assessment_may_2023_round_72.xlsx
  format: null
  id: resource_5379ed75
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 72
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'From 1-7 March 2023, the DTM team in Burundi conducted the 71st round
    of Baseline assessment in 1,353 Collines (Administrative Boundary level 3) and
    identified 73,586 displaced persons (IDPs) in 16,690 households. . Nearly all
    displacements were due to natural disasters (89%) and 11% due to other causes.
    The total number of displaced persons includes the internally displaced persons
    (1) and returnees who remain displaced in country (2): (1) Internally Displaced
    Persons (IDPs): are Burundian nationals who have been forced to flee or forced
    to leave their home or their usual place of residence, in particular as a result
    of armed conflict, situations of violence widespread, human rights violations
    or natural or man-made disasters or to avoid their effects, and which have not
    crossed the internationally recognized borders of a State. For the purpose of
    DTM, only IDPs displaced since 2013 or later are considered IDPs. (2) Returnees
    who became IDPs: Burundian nationals who had been displaced outside the country
    and have since returned (spontaneously or assisted) to Burundi but continue being
    in displacement (because their houses were destroyed or for other reasons)'
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/cf728389-bfc6-4210-af0f-5e454f05ae76/download/hdx_dtm_burundi_baseline_assessment_round_71_mar_2023.xlsx
  format: null
  id: resource_cf728389
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 71
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DTM has identified 75,300 internally displaced persons (IDPs) in 17,128
    households. Almost all displacements were due to natural disasters (89%), while
    11% were due to other reasons.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/b256164e-b979-4692-930b-c689cb62bae5/download/hdx_burundi_fiche_baseline_october_2022.xlsx
  format: null
  id: resource_b256164e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 70
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DTM has identified 83,588 internally displaced persons (IDPs) in 19,047
    households, 91% of the displacement were due to natural disasters and 9% other
    reasons.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/f895a565-e0f2-4d63-baa0-4001ce5d23ed/download/dtm_burundi_-_fiche_baseline_2022_july2022_to_share.xlsx
  format: null
  id: resource_f895a565
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 69
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DTM has identified 84,791 displaced persons in 19,407 households, 91%
    of the displacement were due to natural disasters and 9% other reasons in the
    month of April 2022 covering all 18 provinces of Burundi.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/25abeac3-fd0a-4751-b48b-f5795615ab41/download/dtm_burundi_data_baseline_april_2022_round_68.xlsx
  format: null
  id: resource_25abeac3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 68
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 84,373 internally displaced persons (IDPs) in
    19,413 households, 92% of the displacement were due to natural disasters and 8%
    other reasons in the month of February 2022 covering all 18 provinces of Burundi.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/f43af28a-441e-46b0-9f6b-5c2da47b3b60/download/hdx_bdi_raw-data_baseline_february-2022_to_be_shared_final.xlsx
  format: null
  id: resource_f43af28a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 67
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 113,408 internally displaced persons (IDPs)
    in 25,390 households, 83% of the displacement were due to natural disasters and
    17% other reasons in the month of September 2021 covering all 18 provinces of
    Burundi.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/bdf82785-f445-4a4a-9716-4804c46c3103/download/dtm_burnudi_r66_hdx.xlsx
  format: null
  id: resource_bdf82785
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 66
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DTM has identified 115,981 internally displaced persons (IDPs) in 25,975
    households, 83% of the displacement were due to natural disasters and 17% other
    reasons in the month of August 2021 covering all 18 provinces of Burundi.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/35585318-1882-4e14-83ef-f819442f3249/download/hdx_dtm_burundi_data_commune_august_2021_round_65.xlsx
  format: null
  id: resource_35585318
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 65
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 122,483 internally displaced persons (IDPs)
    in 27,300 households, 84% of the displacement were due to natural disasters and
    16% other reasons in the month of July 2021 covering all 18 provinces of Burundi.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/c242a9f6-7fd7-4e59-a54d-127aba192ad4/download/hdx_dtm_burundi_data_commune_july_2021_round_64.xlsx
  format: null
  id: resource_c242a9f6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 64.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 127,339 internally displaced persons (IDPs)
    in 27,912 households, 85% of the displacement were due to natural disasters and
    15% other reasons in the month of June 2021 covering all 18 provinces of Burundi.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/f2b531e2-8f5a-4a70-907d-b8204edd13ba/download/dtm-burundi-baseline-assessment-round-63.xlsx
  format: null
  id: resource_f2b531e2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 63
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 127,775 internally displaced persons (IDPs)
    in 28,569 households, 85% of the displacement were due to natural disasters and
    15% other reasons in the month of May 2021 covering all 18 provinces of Burundi.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/0cbfc53f-fded-4fc9-973b-536fa5917160/download/dtm-burundi-donnees-commune-may-2021-round-62-hdx.xlsx
  format: null
  id: resource_0cbfc53f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 62
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 107,870 internally displaced persons (IDPs)
    and 25,149 households in the month of April 2021.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/3d753848-cbd1-408e-8368-9313f4cef53c/download/dtm-burundi-donnees-commune-avril-2021-round-61.xlsx
  format: null
  id: resource_3d753848
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 61
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 60)
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/7e6bf058-5fd8-4592-b2b0-9c7ed32ad8bc/download/dtm-burundi-baseline-assessment-round-60.xlsx
  format: null
  id: resource_7e6bf058
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 60
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 59)
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/173740b6-8f13-45e6-8ff9-702d76d2cbf9/download/dtm-burundi-baseline-assessment-round-59.xlsx
  format: null
  id: resource_173740b6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 59
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 58)
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/6b517df8-69a8-422f-b10c-55fc9bfc6041/download/dtm-burundi-baseline-assessment-round-58.xlsx
  format: null
  id: resource_6b517df8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 58
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 57)
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/3eed6862-0c2b-454f-bb66-6722d303b31f/download/dtm-burundi-baseline-assessment-round-57.xlsx
  format: null
  id: resource_3eed6862
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 57
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 56)
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/1f240b4a-86ba-443f-abca-90be15275c08/download/dtm-burundi-baseline-assessment-round-56.xlsx
  format: null
  id: resource_1f240b4a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 56
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 55)
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/982b4fb4-4139-474e-9283-5ca1aa3fc996/download/dtm-burundi-baseline-assessment-round-55.xlsx
  format: null
  id: resource_982b4fb4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 55
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 54)
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/d46ea88c-df6d-4917-bd07-1906389bfac3/download/dtm-burundi-baseline-assessment-round-54.xlsx
  format: null
  id: resource_d46ea88c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 54
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 53)
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/bceb88dd-3c70-4771-a342-fe6744854157/download/dtm-burundi-baseline-assessment-round-53.xlsx
  format: null
  id: resource_bceb88dd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 53
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 52)
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/8542df5e-6968-4756-9a4f-35ab8fe40ce9/download/dtm-burundi-baseline-assessment-round-52.xlsx
  format: null
  id: resource_8542df5e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 52
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 117,239 internally displaced persons (IDPs)
    and 25,754 households in the month of February
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/f2ce573f-46e2-4678-8946-4e4f28655d84/download/dtm-burundi-baseline-assessment-round-51.xlsx
  format: null
  id: resource_f2ce573f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 51
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 116,951 internally displaced persons (IDPs)
    and 25,780 households in the month of November.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/cb26eeba-05eb-4312-85cf-515a1d3e0ecb/download/dtm-burundi-baseline-assessment-round-50.xlsx
  format: null
  id: resource_cb26eeba
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 50
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 104,191 internally displaced persons (IDPs)
    and 24,788 households in the month of November.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/98ade673-44c4-484d-b939-43a057df6c8d/download/dtm-burundi-baseline-assessment-round-49.xlsx
  format: null
  id: resource_98ade673
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 49
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 104,191 internally displaced persons (IDPs)
    and 23,343 households in the month of November.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/50265eef-5cae-4ceb-b85f-3d4a580358a9/download/dtm-burundi-baseline-assessment-round-48.xlsx
  format: null
  id: resource_50265eef
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 48
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 102,722 internally displaced persons (IDPs)
    and 23,009 households in the month of November.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/a0bbc63c-c999-4c85-a410-7167f95a4339/download/dtm-burundi-baseline-assessment-round-47.xlsx
  format: null
  id: resource_a0bbc63c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 47
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 103,352 internally displaced persons (IDPs)
    and 23,162 households in the month of September.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/e0343f83-a392-4e77-ac31-80d7e9fdff7a/download/dtm-burundi-baseline-assessment-round-46.xlsx
  format: null
  id: resource_e0343f83
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 46
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 103,412 internally displaced persons (IDPs)
    and 23,180 households in the month of September.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/d03b1a4a-974e-446e-816e-f1b186f43c6f/download/dtm-burundi-baseline-assessment-round-45.xlsx
  format: null
  id: resource_d03b1a4a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 45
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 106,197 internally displaced persons (IDPs)
    and 23,752 households in the month of August.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/8d641dd9-9a38-4fba-aa64-6411b886260a/download/dtm-burundi-baseline-assessment-round-44.xlsx
  format: null
  id: resource_8d641dd9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 44
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: During July 2019, DTM has identified 109,372 internally displaced persons
    (IDPs) and 24,466 households.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/a80ee75d-63ab-436a-9f45-28fc285b73a9/download/dtm-burundi-baseline-assessment-round-43.xlsx
  format: null
  id: resource_a80ee75d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 43
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'During June 2019, DTM has identified 113,067 IDPs. The main causes
    for the displacements have been: 77 per cent natural disasters and 23 per cent
    other reasons.'
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/7d7bc510-b1b6-4b02-bbd9-6816c70493a1/download/dtm-burundi-baseline-assessment-round-42.xlsx
  format: null
  id: resource_7d7bc510
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 42
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'During May 2019, DTM has identified 115,708 internally displaced persons.
    The main causes for the displacements have been: 76% natural disasters and 24%
    other reasons .'
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/935c262c-b9cd-489e-ac8a-96b3854d1496/download/dtm-burundi-baseline-assessment-round-41.xlsx
  format: null
  id: resource_935c262c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 41
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'During April 2019, DTM has identified 119,890 internally displaced
    persons. The main causes for the displacements have been: 76% natural disasters
    and 24% other reasons .'
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/5fec0071-605a-4d67-80bc-e10f9626b3eb/download/dtm-burundi-baseline-assessment-round-40.xlsx
  format: null
  id: resource_5fec0071
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 40
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'During the month of February, the DTM identified 124,578 internally
    displaced persons and 27,720 families. The main reasons for displacement were:
    natural disasters (75%) and the socio-political situation (25%).'
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/f4d84029-8410-4d65-803d-edd71b2f37b3/download/dtm-burundi-baseline-assessment-round-39.xlsx
  format: null
  id: resource_f4d84029
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 39.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'During the month of February, the DTM identified 130,562 internally
    displaced persons and 28,927 families. The main reasons for displacement were:
    natural disasters (75%) and the socio-political situation (25%).'
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/f0086032-86b8-4a00-8134-1dbd0d6d2511/download/dtm-burundi-baseline-assessment-round-38.xlsx
  format: null
  id: resource_f0086032
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 38
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM identified 134,054 internally displaced persons (IDPs) in 29,536
    IDP households. 76% of IDPs were displaced as a result of natural disasters, while
    24% were displaced due to socio-political situation.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/1728a67c-a8dd-4f04-ba30-fe45fc6ecb22/download/dtm-burundi-baseline-assessment-round-37.xlsx
  format: null
  id: resource_1728a67c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 37
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM identified 139,634 internally displaced persons (IDPs) in 30,742
    IDP households. 77% of IDPs (106,964) were displaced as a result of natural disasters,
    while 23% of IDPs (31,908) were displaced due to socio-political situation.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/102cf9c9-b37e-4854-8745-f8d4afbe746f/download/dtm-burundi-baseline-assessment-round-36.xlsx
  format: null
  id: resource_102cf9c9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 36
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 142,625 internally displaced persons (IDPs)
    amidst 31,593 households. 76% of IDPs (107,908) were displaced as a result of
    natural disasters and 24% of IDPs (33,955) were displaced as a result of sociopolitical
    issues.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/1b3b719e-4328-4450-9d1d-fcdedcf8834a/download/dtm-burundi-baseline-assessment-round-35.xlsx
  format: null
  id: resource_1b3b719e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 35
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: he DTM has identified 147,086 internally displaced persons (IDPs) amidst
    32,527 households. 75% of IDPs (110,460) were displaced as a result of natural
    disasters and 24% of IDPs (34,864) were displaced as a result of sociopolitical
    issues. Oct 2018
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/c7667e30-318b-4aaa-b56e-b65f092eccae/download/dtm-burundi-baseline-assessment-round-34.xlsx
  format: null
  id: resource_c7667e30
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 34
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 151,520 internally displaced persons (IDPs)
    amidst 33,493 households. 75% of IDPs (113,121) were displaced as a result of
    natural disasters and 25% of IDPs (37,639) were displaced as a result of sociopolitical
    issues. Sep 2018
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/549559ae-d2d6-4264-94a1-157450371cbb/download/dtm-burundi-baseline-assessment-round-33.xlsx
  format: null
  id: resource_549559ae
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 33
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DTM has identified 159,152 internally displaced persons (IDPs) amidst
    35,157 households. 74% of IDPs (117,538) were displaced as a result of natural
    disasters and 26% of IDPs (40,856) were displaced as a result of sociopolitical
    issues. Aug 2018
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/5c013c59-8c9d-4f63-af7b-bd5b7e2e5ea9/download/dtm-burundi-baseline-assessment-round-32.xlsx
  format: null
  id: resource_5c013c59
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 32
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM for the month of July 2018 covers all 18 provinces of Burundi,
    and, identified 168,674 IDPs amidst 37,283 households. 74% of IDPs (124,012) were
    displaced as a result of natural disasters and 26% of IDPs (43,926) were displaced
    as a result of sociopolitical issues. 13% of displaced households were headed
    by women, and 3% of households were headed by minors. In addition, 1% of IDPs
    lived with disabilities, 1% of minors were unaccompanied and 2% of IDPs were pregnant
    women.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/2ef6ef55-3149-4248-b91f-e5a014f865f9/download/dtm-burundi-baseline-assessment-round-31.xlsx
  format: null
  id: resource_2ef6ef55
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 31
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 178,267 internally displaced persons (IDPs)
    amidst 39,334 households. 102,034 IDPs (57%) were living with host families, 3,427
    IDPs (2%) were living in displacement sites, 33,309 IDPs (19%) were living in
    emtpy and straw houses, and 39,497 IDPs (22%) were living in rented housing. 73%
    of IDPs (129,965) were displaced as a result of natural disasters and 27% of IDPs
    (47,553) were displaced as a result of sociopolitical issues.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/00239309-6e62-40e0-a6f5-fa1670505380/download/dtm-burundi-baseline-assessment-round-30.xlsx
  format: null
  id: resource_00239309
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 30
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM has identified 187,026 internally displaced persons (IDPs)
    amidst 41,060 households. 108,855 IDPs (58%) were living with host families, 3,552
    IDPs (2%) were living in camps and displacement sites, 34,658 IDPs (19%) were
    living in emtpy and straw houses, and 39,961 IDPs (21%) were living in rented
    housing. 74% of IDPs (137,532) were displaced as a result of natural disasters
    and 26% of IDPs (48,680) were displaced as a result of sociopolitical issues.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/31e6ceef-a5e2-41f9-9099-a885bbca3a5a/download/dtm-burundi-baseline-assessment-round-29.xlsx
  format: null
  id: resource_31e6ceef
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 29
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: April 2018 covers all 18 provinces of Burundi. The DTM has identified
    169,374 internally displaced persons (IDPs) amidst 37,791 households. 90,355 IDPs
    (53%) were living with host families, 3,561 IDPs (2%) were living in camps and
    displacement sites, 33,315 IDPs (20%) were living in emtpy and straw houses, and
    42,143 IDPs (25%) were living in rented housing. 71% of IDPs (119,693) were displaced
    as a result of natural disasters and 29% of IDPs (48,867) were displaced as a
    result of sociopolitical issues.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/16a0823b-ce14-4620-9755-9b304cfa44c7/download/dtm-burundi-baseline-assessment-round-28.xlsx
  format: null
  id: resource_16a0823b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 28
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 174,011 IDPs in 38,538 households were identified. 71% of IDPs were
    displaced as a result of natural disasters, while 29% were displaced because of
    the socio-political situation.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/558850fe-5466-46c8-9639-166dbb8c69f3/download/dtm-burundi-baseline-assessment-round-27.xlsx
  format: null
  id: resource_558850fe
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 27
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset contains IDPs and household information up to Admin2 level.
    39,175 households and 175,936 IDPs identified.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/5b606045-7b42-408c-95c4-0a91ac137689/download/dtm-burundi-baseline-assessment-round-26.csv
  format: null
  id: resource_5b606045
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 26.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset contains IDPs and household information up to Admin2 level.
    39,175 households and 175,936 IDPs identified.
  download_url: https://data.humdata.org/dataset/1eb01fef-133c-4675-b4e9-a76b29511a02/resource/3023e650-ff6f-4273-adfe-b437811d1da9/download/dtm-burundi-baseline-assessment-round-25.xlsx
  format: null
  id: resource_3023e650
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 25
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DTM Burundi identified 179,901 IDPs comprising 40,272 households. 81%
    of IDPs were women and youth under 18 years old, and 29% of IDPs were children
    under 5 years old. 7,371 IDPs (4%) were living in camps and displacement sites,
    94,268 IDPs (53%) were living with host families, 31,371 IDPs (17%) were living
    in emtpy and straw houses, and 46,891 IDPs (26%) were living in rented housing.
    68% of IDPs were displaced as a result of natural disasters and 32% of IDPs were
    displaced as a result of sociopolitical issues.
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_24_0.xlsx?file=1&type=node&id=3176
  format: null
  id: resource_a996ae84
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 24
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 187,626 IDPs in 42,416 households were identified. 69% of IDPs were
    displaced as a result of natural disasters, while 31% were displaced because of
    the sociopolitical situation.
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_23.xlsx?file=1&type=node&id=3174
  format: null
  id: resource_c10b542c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 23
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 189,000 IDPs comprising 42,565 households. 80% of IDPs were women and
    youth under 18 years old, and 30% of IDPs were children under 5 years old. 7,308
    IDPs were living in camps and displacement sites, 104,118 IDPs were living with
    host families, 26,252 IDPs were living in emtpy houses, and 51,322 IDPs were living
    in rented housing. 123,510 IDPs were displaced as a result of natural disasters
    and 64,673 IDPs were displaced as a result of sociopolitical issues.
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_22.xlsx?file=1&type=node&id=3177
  format: null
  id: resource_75c1cf37
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 22
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 188,294 IDPs in 42,234 households were identified. 66% of IDPs were
    displaced as a result of natural disasters, while 34% were displaced because of
    the sociopolitical situation.
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_21.xlsx?file=1&type=node&id=3178
  format: null
  id: resource_a6b97eb6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 21
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 191,806 internally displaced persons (IDPs) and 42,859 households in
    the provinces of Gitega, Cankuzo, Bujumbura Rural, Rutana, Makamba, Ruyigi, Muyinga,
    Kirundo, Cibitoke, Rumonge, Bubanza, Bururi, Kayanza, Muramvya, Mwaro, Ngozi and
    Karusi. In terms of reasons for displacement, 66% cited natural disasters while
    34% of migrants cited socio-political reasons. Women and children represented
    52% of the displaced population. The large majority of IDPs (56%) live in host
    families, followed by 26% who live in rented houses.
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_20.xlsx?file=1&type=node&id=3179
  format: null
  id: resource_3b39793f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 20
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 19)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_19_2017.xlsx?file=1&type=node&id=2217
  format: null
  id: resource_00e52413
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 19
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 18)
  download_url: https://displacement.iom.int/system/tdf/datasets/IOM_DTM_Dataset_Burundi_Round_18_201709_BA.xlsx?file=1&type=node&id=2218
  format: null
  id: resource_85bda87e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 18
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 17)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_17_2017.xlsx?file=1&type=node&id=1490
  format: null
  id: resource_6652cfae
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 17
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 16)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_16_2017.xlsx?file=1&type=node&id=1489
  format: null
  id: resource_684d6f48
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 16
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 15)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_15_2017.xlsx?file=1&type=node&id=1488
  format: null
  id: resource_e538ae86
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 15
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 14)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_14_20170324.xlsx?file=1&type=node&id=1487
  format: null
  id: resource_810bcc5e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 14
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 13)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_13_20170131.xlsx?file=1&type=node&id=264
  format: null
  id: resource_321eddd9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 13
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 12)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_12_20161231_0.xlsx?file=1&type=node&id=263
  format: null
  id: resource_f13dc66f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 12
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 11)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_11_20161130.xlsx?file=1&type=node&id=262
  format: null
  id: resource_482e39d6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 11
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 10)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_10_20161031.xlsx?file=1&type=node&id=261
  format: null
  id: resource_9dd62922
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 10
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 9)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_09_20160930_0.xlsx?file=1&type=node&id=260
  format: null
  id: resource_941cb651
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 9
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 8)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_08_20160830.xlsx?file=1&type=node&id=228
  format: null
  id: resource_3f2b73cb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 8
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 7)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi_Baseline_Round_07_20160731.xlsx?file=1&type=node&id=221
  format: null
  id: resource_00e3c4fd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 7
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 6)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi%20Baseline%20Round%206.xlsx?file=1&type=node&id=3251
  format: null
  id: resource_68fd59ce
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 6
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 5)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi%20Baseline%20Round%205.xlsx?file=1&type=node&id=3250
  format: null
  id: resource_f6cedfd6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 5
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 4)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi%20Baseline%20Round%204.xlsx?file=1&type=node&id=3249
  format: null
  id: resource_fae8ee36
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 4
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 3)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi%20Baseline%20Round%203.xlsx?file=1&type=node&id=3248
  format: null
  id: resource_39b4d227
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 3
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM] (DTM
    Burundi Baseline Assessment Round 2)
  download_url: https://displacement.iom.int/system/tdf/datasets/Burundi%20Baseline%20Round%202.xlsx?file=1&type=node&id=3247
  format: null
  id: resource_734b41ac
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Baseline Assessment Round 2
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bdi_iom_displacementidpsbaselinea_2016
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
  end: '2025-07-02'
  start: '2016-01-31'
temporal_resolution: null
title: Burundi Displacement - [IDPs] - Baseline Assessment [IOM DTM]
version: null
vulnerability: null
---
