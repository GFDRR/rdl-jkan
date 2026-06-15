---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/kenya-displacement-baseline-multi-sectoral-location-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/kenya-displacement-baseline-multi-sectoral-location-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/kenya-displacement-baseline-multi-sectoral-location-assessment-iom-dtm
dataset_id: rdls_lss-ken_iom_displacementbaselinemulti_2022
description: 'The assessment of drought-induced mobility dynamics, as well as the
  MSLA are aimed at collecting baseline information one mobility trends and most urgent
  sectoral needs of the target mobile population groups and host communities.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/kenya-displacement-baseline-multi-sectoral-location-assessment-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Baseline and Multi-Sectoral Location Assessment (BA/MSLA) data collected
    through IOM DTM standard methodology using key informant interviews across five
    drought-affected counties in northern Kenya (Samburu, Marsabit, Isiolo, Turkana,
    Garissa). Data captures drought-induced mobility patterns including departures,
    arrivals, returnees, pastoral livelihood changes, and immediate sectoral needs
    (shelter, WASH, health, education) of mobile populations and host communities.
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
- href: https://data.humdata.org/dataset/kenya-displacement-baseline-multi-sectoral-location-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Drought-induced displacement of households across pastoral communities
      in northern Kenya
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
    description: Multi-sectoral needs assessment of drought-affected mobile populations
      and host communities
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
  url: https://dtm.iom.int/about/methodological-framework
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: During this round, the data collection was conducted in 3 sub-counties
    of Samburu county in 16 wards across 110 sub-locations covering 686 settlements.
    From 16 to 28 January 2023, the DTM team in Kenya has identified 7,879 returnees
    households, 9,736 arrival households, 4,772 returnee households and 15 foreign
    national households.
  download_url: https://data.humdata.org/dataset/db3e1a76-76d8-4206-9e5e-382336c51472/resource/501b929d-012b-4557-b5bf-2003fd4e3661/download/dtm_kenya_ba_msla_round_1_samburu_county_jan_2023_ext.xlsx
  format: null
  id: resource_501b929d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Kenya - BA/MSLA - Samburu County - Round 1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The data collection was conducted across the entire nine sub-counties
    of Marsabit County in 19 Wards, 134 sub-locations and 1,045 settlements.
  download_url: https://data.humdata.org/dataset/db3e1a76-76d8-4206-9e5e-382336c51472/resource/bfa6de7f-2bd3-469f-9371-9c6ad359f3e2/download/dtm_kenya_ba_msla_round_1_marsabit_county_dec_2022.xlsx
  format: null
  id: resource_bfa6de7f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Kenya - BA/MSLA - Marsabit County - Round 1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The data collection was conducted across the entire three sub-counties
    of Isiolo County in 10 Wards, 88 sub-locations and 566 settlements.
  download_url: https://data.humdata.org/dataset/db3e1a76-76d8-4206-9e5e-382336c51472/resource/512b5c4c-0440-46fc-91b7-57134ade648a/download/dtm_kenya_ba_msla_round_1_isiolo_county_dec_2022.xlsx
  format: null
  id: resource_512b5c4c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Kenya - BA/MSLA - Isiolo County - Round 1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The assessment was conducted across the entire Turkana County by enumerators
    in 30 Wards, 174 sublocations and 1,867 settlements. A total of 53 enumerators
    and five team leaders who are familiar with the local and administrative contexts
    were locally engaged from each sub-location, through the support of LOKADO. The
    local enumerators and team leaders were trained by IOM on DTM data collection
    prior to field deployment. The data collection process was implemented by LOKADO
    and closely monitored by IOM. The enumerators have accessed 163 sub-locations
    and carried out face-to-face interviews with the key informants. For the 11 sub-locations
    that were not accessible due to insecurity, data collection was conducted by interviewing
    key informants over mobile phones. The assessment has excluded refugee camps in
    Kakuma to avoid double counting of affected mobile population. For the assessments,
    571 key informants were interviewed covering a total of 1,867 settlements in Turkana
    County.
  download_url: https://data.humdata.org/dataset/db3e1a76-76d8-4206-9e5e-382336c51472/resource/562aad8a-2d68-4560-8c8b-237459958183/download/dtm_kenya_b2_baseleine_multi_sectoral_assessment_nov_2022_v3.xlsx
  format: null
  id: resource_562aad8a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Kenya - BA/MSLA - Turkana County - Round 1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'DTM''s mobility tracking baseline area assessment was conducted in
    coordination with Garissa County Government, County Commissioner''s office, and
    NDMA from 5 to 19 September 2022 in Garissa. The assessment was conducted at two
    levels - ward level and settlement level, using key informant interviews. DTM
    assessed all 30 wards and 356 settlements in Garissa. Out of the 356 settlements,
    IOM enumerators could physically access 350 locations and carried out face-to-face
    interviews with key informants. For the six settlements that were not accessible
    data collection was conducted by interviewing key informants over the phone. The
    assessment excluded refugee camps such as Dadaab to avoid double counting of affected
    mobile population. Information was collected on the following population categories:
    - Absentees: Residents of the settlement who have left the settlement because
    of drought (death of animals, lack of food, lack of water, search for services),
    resource-based conflict, flash floods or seasonal floods, or fires. - Arrivals:
    Persons who have left their settlement of habitual residence and arrived to the
    location assessed because of drought (death of animals, lack of food, lack of
    water, search for services), resource-based conflict, flash floods or seasonal
    floods, or fires. - Pastoralist drop-outs: Agro-pastoralist who have lost their
    livestock or whose land has become unproductive and have therefore become destitute.
    - Returnees: People that had left the settlement due to drought, but came back
    within the last two years. - Foreign nationals: Non-Kenyan nationals that have
    arrived in the settlement of assessment because of drought (death of animals,
    lack of food, lack of water, search for services), resourcebased conflict, flash
    floods or seasonal floods, or fires This includes migrants who cannot return,
    continue their journey or who are destitute in the location of assessmen'
  download_url: https://data.humdata.org/dataset/db3e1a76-76d8-4206-9e5e-382336c51472/resource/8fbb192a-ec8c-49c8-a4a4-a04eae058b72/download/dtm_kenya_b2_baseline_assessment_garissa_county.xlsx
  format: null
  id: resource_8fbb192a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Kenya - BA/MSLA - Garissa County - Round 1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ken_iom_displacementbaselinemulti_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-01-28'
  start: '2022-09-05'
temporal_resolution: null
title: Kenya Displacement - Baseline/Multi-Sectoral Location Assessment [IOM DTM]
version: null
vulnerability: null
---
