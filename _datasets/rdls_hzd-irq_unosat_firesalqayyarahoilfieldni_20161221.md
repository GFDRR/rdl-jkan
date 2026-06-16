---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-and-14-december-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-and-14-december-2016
dataset_id: rdls_hzd-irq_unosat_firesalqayyarahoilfieldni_20161221
description: 'This map illustrates satellite-detected fires and smoke plumes at oil
  wells south of Mosul, and also east of Baiji, Iraq. The Mosul fires began with an
  initial fire at one or two wells on 8 May 2016, lasting less than one day, and intermittently
  burned in June. The current fire complex began on 3 July with daily fire detections
  occurring until about 12 July, when the fires greatly increased in number and continued
  to burn to the present at that scale. The fires east of Baiji have been active since
  early January 2016. The frequency of smoke plumes (in days) is symbolized in shades
  of red and yellow, and was calculated using daily MODIS satellite images collected
  between 18 July and 14 December, 2016. Note that as the plume dissipates then areas
  of thinner smoke are not detected in this process. The inset on the top right corner
  shows the thermal data from a Landsat image collected on 7 December, indicating
  the Mosul fires in white. The inset on the top left corner, from 6 December, shows
  the same area in false color, displaying the near infrared band in red. Additionally,
  precipitation data from NASA''s IMERG algorithm was included to evaluate instances
  of rainfall intersecting the smoke plume. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR - UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-and-14-december-2016]'
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
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared multi-temporal satellite imagery
    of the Al Qayyarah oil field to detect active fires and quantify smoke plume frequency
    (in days) at specific well locations. Fire detections were mapped spatially with
    smoke frequency symbolized by color intensity, providing an empirical hazard dataset
    derived from remote sensing observations between July and December 2016.
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
- href: https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-and-14-december-2016
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
  description: Iraq - Fires at the Al Qayyarah oil field, Nineveh Governorate, between
    18 July and 14 December, 2016 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_South_Mosul_oil_fires.gdb.zip
  format: Geodatabase
  id: resource_5d18b42a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_South_Mosul_oil_fires.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Fires at the Al Qayyarah oil field, Nineveh Governorate, between
    18 July and 14 December, 2016 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_South_Mosul_oil_fires.zip
  format: null
  id: resource_60056eb5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_South_Mosul_oil_fires.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-irq_unosat_firesalqayyarahoilfieldni_20161221
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-12-21'
temporal_resolution: null
title: Iraq - Fires at the Al Qayyarah oil field, Nineveh Governorate, between 18
  July and 14 December, 2016
version: null
vulnerability: null
---
