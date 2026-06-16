---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2013-tropical-cyclone-3a
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2013-tropical-cyclone-3a
dataset_id: rdls_he-som_icpac_districtshit2013tropicalc_201311
description: 'This layer shows Somalia Disricts struck by 2013 TC3A. They include,
  Bossaso, Bandarbeyla, Caluula, Iskushuban, Qandala, Qardho, Garoowe and Eyl District.
  On 8 November 2013, TC3A formed off the north-east coast of Somalia across the Indian
  Ocean, moving directly towards the coast of the country during the following days.
  On November 11, 2013 TC3A struck near the border of the Nugal and Bari regions and
  caused severe flash flooding. The storm produced a maximum wind speed of 74kph(46mph)
  and (100-200)mm of rainfall. 2013 TC3A was the deadliest tropical cyclone on record
  in Somalia, killing more than 162 people. The depression also destroyed over 1,000
  houses, displaced tens of thousands of nomads, and killed millions of livestock.
  It was estimated that overall, 142,380 persons were affected by the disasters, with
  8,523 households being worst hit and 1,435 households having lost all their livestock.
  It was reported that there were approximately 80 deaths mostly of children and the
  elderly who were most vulnerable to hypothermia and exposure. Makeshift structures
  for pastoralists were conspicuously absent or just frames, likely destroyed or damaged
  by high winds and rains. Numerous water sources were flooded, no longer serviceable
  and or contaminated in some areas. There were unconfirmed disease outbreaks and
  contamination of water sources from decaying animal remains. Thousands of livestock
  were reported dead as a consequence of icy rain, which was noted in the aerial assessment.
  FAO estimated 800,000 livestock were in the affected area. Anecdotal evidence suggested
  a less than 10 per cent survival rate for livestock in the hardest hit areas.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2013-tropical-cyclone-3a]'
details: null
exposure:
- asset_type:
    description: Population in Somalia districts exposed to tropical cyclone 2013
      TC3A
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: probabilistic
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
license: CC-BY-4.0
lineage:
  description: Post-event observational data from ICPAC documenting the 2013 Tropical
    Cyclone 3A track, wind speeds (74 kph maximum), and rainfall (100-200 mm) across
    Somalia districts. Administrative boundaries of affected districts were delineated
    and compiled into vector geospatial formats to represent the spatial extent of
    cyclone impact.
  sources:
  - id: source_1
    license: null
    name: IGAD Climate Prediction and Applications Center (ICPAC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2013-tropical-cyclone-3a
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2013_TC3A&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. This layer shows Somalia Disricts struck by 2013 TC3A.
    They include, Bossaso, Bandarbeyla, Caluula, Iskushuban, Qandala, Qardho, Garoowe
    and Eyl District. On 8 November 2013, TC3A formed off the north-east coast of
    Somalia across the Indian Ocean, moving directly towards the coast of the country
    during the following days. On November 11, 2013 TC3A struck near the border of
    the Nugal and Bari regions and caused severe flash flooding. The storm produced
    a maximum wind speed of 74kph(46mph) and (100-200)mm of rainfall.
  download_url: null
  format: null
  id: resource_cb8521e5
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2013 Tropical Cyclone 3A GeoJSON
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2013_TC3A&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. This layer shows Somalia Disricts struck by
    2013 TC3A. They include, Bossaso, Bandarbeyla, Caluula, Iskushuban, Qandala, Qardho,
    Garoowe and Eyl District. On 8 November 2013, TC3A formed off the north-east coast
    of Somalia across the Indian Ocean, moving directly towards the coast of the country
    during the following days. On November 11, 2013 TC3A struck near the border of
    the Nugal and Bari regions and caused severe flash flooding. The storm produced
    a maximum wind speed of 74kph(46mph) and (100-200)mm of rainfall.
  download_url: null
  format: null
  id: resource_04a99762
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2013 Tropical Cyclone 3A Zipped Shapefile
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2013_TC3A&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. This layer shows Somalia Disricts struck by 2013 TC3A. They
    include, Bossaso, Bandarbeyla, Caluula, Iskushuban, Qandala, Qardho, Garoowe and
    Eyl District. On 8 November 2013, TC3A formed off the north-east coast of Somalia
    across the Indian Ocean, moving directly towards the coast of the country during
    the following days. On November 11, 2013 TC3A struck near the border of the Nugal
    and Bari regions and caused severe flash flooding. The storm produced a maximum
    wind speed of 74kph(46mph) and (100-200)mm of rainfall.
  download_url: null
  format: null
  id: resource_d5f4b509
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2013 Tropical Cyclone 3A CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2013_TC3A&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. This layer shows Somalia Disricts struck by 2013 TC3A.
    They include, Bossaso, Bandarbeyla, Caluula, Iskushuban, Qandala, Qardho, Garoowe
    and Eyl District. On 8 November 2013, TC3A formed off the north-east coast of
    Somalia across the Indian Ocean, moving directly towards the coast of the country
    during the following days. On November 11, 2013 TC3A struck near the border of
    the Nugal and Bari regions and caused severe flash flooding. The storm produced
    a maximum wind speed of 74kph(46mph) and (100-200)mm of rainfall.
  download_url: null
  format: null
  id: resource_01f748c6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2013 Tropical Cyclone 3A Excel
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-som_icpac_districtshit2013tropicalc_201311
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
  end: '2013-11-13'
  start: '2013-11-08'
temporal_resolution: null
title: Somalia Districts hit by 2013 Tropical Cyclone 3A
version: null
vulnerability: null
---
