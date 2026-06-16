---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2010-tropical-cyclone-bandu
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2010-tropical-cyclone-bandu
dataset_id: rdls_hl-som_icpac_districtshit2010tropicalc_201005
description: 'Tropical Cyclone Bandu was named after Tropical Storm 02A moving into
  the Gulf of Aden. This layer shows TC Bandu hitting Bossaso District on May 21,
  2010. Bandu had maximum sustained winds near 45 knots (52 mph) and was 50 miles
  north-northwest of Cape Guardafui, Somalia. Tropical Storm Bandu resulted in flooding,
  and displaced approximately 12,000 people in Bari,17000 along Shabelle River and
  2,000 people in Jamaame town, Lower Juba Region, as well as Afgooye and Kurtunwaarey
  districts, Lower Shabelle Region. In response to identified humanitarian needs,
  the U.N. Children&rsquo;s Fund (UNICEF) and non-governmental organization (NGO)
  partners provided support for garbage collection and WASH activities. In addition,
  UNHCR distributed blankets and plastic sheeting to flood-affected residents of Bossaso
  town, Bari Region.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2010-tropical-cyclone-bandu]'
details: null
exposure: []
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Observed tropical cyclone track data from ICPAC for Cyclone Bandu (May
    2010) was spatially intersected with Somalia administrative district boundaries
    to identify affected areas. Post-event displacement figures from humanitarian
    response assessments were compiled for affected regions including Bari, Shabelle
    River, Lower Juba, and Lower Shabelle, capturing both direct wind impacts and
    secondary flooding effects.
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
- href: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2010-tropical-cyclone-bandu
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement from Tropical Cyclone Bandu across Bari,
      Shabelle River, Lower Juba, and Lower Shabelle regions
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
        metric: displaced
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displacement from flooding triggered by Tropical Cyclone
      Bandu
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2010_TCBandu&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. Tropical Cyclone Bandu was named after Tropical
    Storm 02A moving into the Gulf of Aden. This layer shows TC Bandu hitting Bossaso
    District on May 21, 2010. Bandu had maximum sustained winds near 45 knots (52
    mph) and was 50 miles north-northwest of Cape Guardafui, Somalia.
  download_url: null
  format: null
  id: resource_474d96dd
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2010 Tropical Cyclone Bandu Zipped Shapefile
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2010_TCBandu&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. Tropical Cyclone Bandu was named after Tropical Storm 02A
    moving into the Gulf of Aden. This layer shows TC Bandu hitting Bossaso District
    on May 21, 2010. Bandu had maximum sustained winds near 45 knots (52 mph) and
    was 50 miles north-northwest of Cape Guardafui, Somalia.
  download_url: null
  format: null
  id: resource_9050d73b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2010 Tropical Cyclone Bandu CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2010_TCBandu&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. Tropical Cyclone Bandu was named after Tropical Storm 02A
    moving into the Gulf of Aden. This layer shows TC Bandu hitting Bossaso District
    on May 21, 2010. Bandu had maximum sustained winds near 45 knots (52 mph) and
    was 50 miles north-northwest of Cape Guardafui, Somalia.
  download_url: null
  format: null
  id: resource_268cc0e1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2010 Tropical Cyclone Bandu Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2010_TCBandu&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. Tropical Cyclone Bandu was named after Tropical Storm
    02A moving into the Gulf of Aden. This layer shows TC Bandu hitting Bossaso District
    on May 21, 2010. Bandu had maximum sustained winds near 45 knots (52 mph) and
    was 50 miles north-northwest of Cape Guardafui, Somalia.
  download_url: null
  format: null
  id: resource_b8c079dc
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2010 Tropical Cyclone Bandu GeoJSON
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_icpac_districtshit2010tropicalc_201005
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
  end: '2010-05-23'
  start: '2010-05-19'
temporal_resolution: null
title: Somalia Districts hit by 2010 Tropical Cyclone Bandu
version: null
vulnerability: null
---
