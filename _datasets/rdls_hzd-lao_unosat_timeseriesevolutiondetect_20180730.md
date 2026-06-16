---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/time-series-evolution-satellite-detected-water-extent-over-sanamxay-district-attapeu-province-lao-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/time-series-evolution-satellite-detected-water-extent-over-sanamxay-district-attapeu-province-lao-
dataset_id: rdls_hzd-lao_unosat_timeseriesevolutiondetect_20180730
description: 'This map illustrates a time series analysis of the evolution of satellite-detected
  surface waters in Sanamxay district, Attapeu province, based on satellite data collected
  on 13, 25 and 29 July 2018. Within the current map extent, on 13 July 2018, before
  the collapse of the dam, a total surface of 47,717 ha was detected as inundated
  and the reservoir controlled by the dam was full of water. As of 25 July 2018, two
  days after the dam collapsed, an additional surface of 7,531 ha of inundated areas
  were detected, representing an increase of the surface waters of 16%. On 29 July
  2018, floodwaters are receding, especially along the riverbanks of Xe Kong River.
  A total surface of 30,435 ha was detected as inundated at that date, representing
  a decrease of the surface waters of 45%. The reservoir that was controlled by the
  dam has continuously decreased in its size since the dam collapsed. It is likely
  that flood waters have been systematically underestimated along highly vegetated
  areas, along main riverbanks and within built-up urban areas because of the special
  characteristics of the used satellite data. Additional optical VHR data are needed
  to validate analysis over areas covered by mud, hardly detected by radar data. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/time-series-evolution-satellite-detected-water-extent-over-sanamxay-district-attapeu-province-lao-]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared satellite imagery acquired on 13, 25, and
    29 July 2018 to detect changes in surface water extent following the Xe-Pian Xe-Namnoy
    dam collapse. Water bodies were classified and mapped as polygons with area calculations
    in hectares and square meters, providing empirical post-event flood extent observations.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/time-series-evolution-satellite-detected-water-extent-over-sanamxay-district-attapeu-province-lao-
  rel: source
loss: null
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
  description: 'Time series: evolution satellite detected water extent over Sanamxay
    District, Attapeu Province, Lao PDR (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LA/FL20180723LAO/FL20180723LAO_shp.zip
  format: null
  id: resource_7a7fdda5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180723LAO_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-lao_unosat_timeseriesevolutiondetect_20180730
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-07-30'
temporal_resolution: null
title: 'Time series: evolution satellite detected water extent over Sanamxay District,
  Attapeu Province, Lao PDR'
version: null
vulnerability: null
---
