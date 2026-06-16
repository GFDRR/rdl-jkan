---
attributions:
- entity:
    affiliation: null
    email: null
    name: Tropical Storm Risk - UCL
    url: https://data.humdata.org/dataset/philippines-typhoon-mangkhut-priority-index-forecasted-damage
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/philippines-typhoon-mangkhut-priority-index-forecasted-damage
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/philippines-typhoon-mangkhut-priority-index-forecasted-damage
dataset_id: rdls_hl-phl_nlrc510_typhoonmangkhutpriorityin_20180913
description: 'Update 15/09 (POST-EVENT) Now that the typhoon has passed the country,
  the model is not run with forecasted wind speeds and typhoon track any more, but
  with actual estimated wind speeds and typhoon track. They come from the same source
  (Tropical Storm Risk - UCL), and are of the exact same format. All output (map in
  PDF, data in Excel and in Shapefile) is of the exact same format and interpretation.
  Full methodology 1. Based on existing Priority Index model: 510 has previously developed
  the Priority Index model for typhoons in the Philippines One day after a typhoon
  has passed the Philippines .. .. the model predicts ''% of completely damaged houses''
  per municipality Based on 12 large typhoons in the last 5 years in the Philippines,
  for which detailed damage reports were available through NDRRMC (https://www.ndrrmc.gov.ph/)
  For these same events, we also collected possible explanatory indicators, such as
  wind speed (event-specific) and building materials of houses (PH national census).
  We built a statistical model, which could explain differences in damage on the basis
  of differences in wind speed and building materials (etc.) When dividing all municipalities
  in 5 equal damage classes (class 1 being the 20% municipalities with lowest damage;
  class 5 the 20% with highest damage) .. .. we found that in 73% of the cases we
  are at most 1 class off. 2. Mangkhut methodology: In the case of typhoon Mangkhut,
  we are dealing with an upcoming typhoon, which is still awaiting landfall on Saturday
  15/09. This is a new situation, which requires the following noteworthy changes
  in methodology. Our wind speed source (UCL Tropical Storm Risk) has - in addition
  to post-event wind speed data as used above - also forecast wind speed data for
  5 days ahead. This forecasted wind speed (and typhoon track) are plugged as input
  into the above-mentioned prediction model, which - still in combination with building
  materials - lead to the predicted damage class per municipality that can be seen
  in the map. Note that the results are strongly dependent on the input of windspeed,
  which is itself still an unknown. (see accuracy below). 3. How to use this product:
  The map contains damage classes (1-5) per municipality. As such, we advise to put
  priority on municipalities in damage class 5, and depending on available resources
  continue with class 4, etc. This damage class is based on ''% of houses that are
  completely damaged''. As priority might also be based on exposure and vulnerability,
  we have added to the Excel a couple of relevant indicators, from the Community Risk
  Assessment dashboard . PRC can decide if and how to combine these various features.
  If needed, 510 can be asked for assistance of course. 4. Important notes: ACCURACY:
  it should be realized that during the course of the coming 3 days, the typhoon might
  change course, or increase/decrease in terms of strength. This will affect the quality
  of these predictions. The accuracy figure of 73% that is mentioned in the post-event
  case should be seen as an upper bound. Given the added inaccuracy of wind speed,
  the overall accuracy will be lower. This damage prediction is only about completely
  damaged houses, not about partially damaged houses. We only included municipalities
  that are within 100km of the forecasted typhoon track, as we have seen from previous
  typhoons (with comparable wind speeds) that damage figures outside of this area
  are low. 5. Sources The wind speed is provided by Tropical Storm Risk (University
  College London). It is the ''maximum 1-minute sustained wind speed''. An average
  of this is calculated per municipality. (Latest forecast date: 2018-09-14 00:00
  UT >> 7:00AM Manila time) Typhoon track (from which ''distance to typhoon track''
  per municipality is calculated), is provided by UCL as well. (Latest forecast date:
  2018-09-14 00:00 UT >> 7:00AM Manila time) Additionally, various wall and roof type
  categories from the Philippines national census. The model uses 2010 census data,
  as it was developed using this data (2015 census data on municipality level only
  became available in 2018). The 2015 census data could not be easily plugged in,
  because of some differences in roof/wall categories. We believe that this would
  not change the result much though, as even if there are large differences from 2010
  to 2015, these would still be dominated by wind speed effects in the model. All
  additional indicators, that are added to the Excel table (population, poverty) are
  derived from the Community Risk Assessment dashboard (Go to this link and click
  ''Export to CSV'' on top-right.) The sources for these indicators can be found in
  the dashboard itself.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/philippines-typhoon-mangkhut-priority-index-forecasted-damage]'
details: 'Accuracy: NDRRMC publishes official data; they can only publish the official
  data when it is validated by their local counterparts (LGU or regional officials).'
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The Priority Index model integrates actual post-event wind speed and
    typhoon track data from Tropical Storm Risk (UCL) with pre-existing structural
    vulnerability relationships to estimate direct building damage classifications
    at the municipal level across the Philippines for Typhoon Mangkhut.
  sources:
  - id: source_1
    license: null
    name: Tropical Storm Risk - UCL
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Netherlands Red Cross - 510
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-typhoon-mangkhut-priority-index-forecasted-damage
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Estimated direct building damage classification by municipality based
      on modeled wind speeds from Typhoon Mangkhut
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: damage
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
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
  url: https://www.ndrrmc.gov.ph/
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://dashboard.510.global/#!/community_risk
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: https://dashboard.510.global/#!/community_risk?country=PHL&admlevel=3&metric=risk_score&parent_code=PH023100000,PH021500000,PH143200000,PH140100000,PH148100000,PH012800000&view=map
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: LATEST POST-EVENT Dataset of Damage estimation per municipality on
    15 september 2018, 2pm PH time. Pcoded. Based on actual estimated wind speeds
    now, instead of forecasted wind speeds.
  download_url: https://data.humdata.org/dataset/91a37f38-19a6-4ab5-a4c2-e8e3571fff81/resource/f45f111a-52a0-408e-8e87-dc92e7fb9c47/download/post-event_510_mangkhut_damage_estimation_data.xlsx
  format: null
  id: resource_f45f111a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: POST-EVENT_510_Mangkhut_damage_estimation_data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: LATEST POST-EVENT Damage estimation per municipality on 14 september
    2018, 8pm PH time , pcoded in shapefile, including estimated damage class & wind
    speed & distance to typhoon track.
  download_url: https://data.humdata.org/dataset/91a37f38-19a6-4ab5-a4c2-e8e3571fff81/resource/7ab936e2-5091-4e71-8243-e62e31476266/download/post-event_510_mangkhut_damage_estimation.zip
  format: null
  id: resource_7ab936e2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: POST-EVENT_510_Mangkhut_damage_estimation.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: LATEST PRE-EVENT Damage prediction per municipality on 14 september
    2018, 8pm PH time , pcoded.
  download_url: https://data.humdata.org/dataset/91a37f38-19a6-4ab5-a4c2-e8e3571fff81/resource/a9ea3c71-8926-436c-8af4-7f81e9b95284/download/latest_510_mangkhut_damage_prediction_data_friday1409_update2.xlsx
  format: null
  id: resource_a9ea3c71
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LATEST_510_Mangkhut_damage_prediction_data_friday1409_update2.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: LATEST PRE-EVENT Damage prediction per municipality on 14 september
    2018, 8pm PH time , pcoded in shapefile, including Predicted damage class & Forecasted
    wind speed.
  download_url: https://data.humdata.org/dataset/91a37f38-19a6-4ab5-a4c2-e8e3571fff81/resource/6fa7926a-a827-4e87-86d4-e093171ad8e2/download/latest_510_mangkhut_damage_prediction_shapefile_friday2.zip
  format: null
  id: resource_6fa7926a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LATEST_510_Mangkhut_damage_prediction_shapefile_friday2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: OLDER PRE-EVENT Damage prediction per municipality on 14 september
    2018, 7am PH time , pcoded.
  download_url: https://data.humdata.org/dataset/91a37f38-19a6-4ab5-a4c2-e8e3571fff81/resource/c5489e56-e2c0-4c1d-95db-80c974dc4dc9/download/510_mangkhut_damage_prediction_data_friday1409.xlsx
  format: null
  id: resource_c5489e56
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 510_Mangkhut_damage_prediction_data_friday1409.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: OLDER PRE-EVENT Damage prediction per municipality on 13 september
    2018, 1pm PH time , pcoded.
  download_url: https://data.humdata.org/dataset/91a37f38-19a6-4ab5-a4c2-e8e3571fff81/resource/981ae296-fc03-4caf-966e-a07145ee9291/download/510_mangkhut_damage_prediction_data_thursday1309.xlsx
  format: null
  id: resource_981ae296
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 510_Mangkhut_damage_prediction_data_thursday1309.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: OLDER PRE-EVENT Damage prediction per municipality on 14 september
    2018, 7am PH time , pcoded in shapefile, including Predicted damage class & Forecasted
    wind speed.
  download_url: https://data.humdata.org/dataset/91a37f38-19a6-4ab5-a4c2-e8e3571fff81/resource/f2dba2d4-2065-4de8-9c46-7a8ef22e0e2a/download/510_mangkhut_damage_prediction_shapefile.zip
  format: null
  id: resource_f2dba2d4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 510_Mangkhut_damage_prediction_shapefile.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-phl_nlrc510_typhoonmangkhutpriorityin_20180913
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-09-13'
temporal_resolution: null
title: Philippines - Typhoon Mangkhut - Priority Index (Estimated damage per municipality)
version: null
vulnerability: null
---
