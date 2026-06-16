---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-2015-tropical-cyclone-megh-path
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-2015-tropical-cyclone-megh-path
dataset_id: rdls_hl-som_icpac_2015tropicalcyclonemeghpa_201511
description: 'This layer shows the movement path for 2015 Tropical Cyclone Megh. Following
  Tropical Cyclone Chapala, new tropical cyclone Megh originated from the Arabian
  Sea causing even more rains in parts of Bari region in Puntland and Somaliland.
  The storm produced a maximum windspeed of 110knots. Areas affected included: Af
  Kalahay, Alula, Bareda, BiyoCade, Boolimoog, Dhurbo, Fagoora, Geesalay, Murcanyo,
  Sayn Weyn, Sayn Yar, Toxin and Xaabo. Re-estimated population figures after Tropical
  Megh, showed 4.9 million people were in need of assistance, 308,700 children under-5
  were acutely malnourished, of which 55,800 were severely malnourished and 1.1 million
  remain in a protracted internal displacement situation.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/icpac-geonode-2015-tropical-cyclone-megh-path]'
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
  description: Observed tropical cyclone track data collected and compiled by ICPAC
    from meteorological monitoring during the 2015 event. The dataset contains sequential
    position, wind speed, and pressure measurements along the cyclone path. Post-event
    impact figures (affected population and malnutrition cases) were compiled from
    humanitarian assessments conducted after the storm affected Puntland and Somaliland
    regions.
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
- href: https://data.humdata.org/dataset/icpac-geonode-2015-tropical-cyclone-megh-path
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Post-event population affected by 2015 Tropical Cyclone Megh estimated
      at 4.9 million people in need of assistance
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
        metric: exposure
        modelling: simulated
        type: total
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Acute malnutrition in children under-5 following 2015 Tropical Cyclone
      Megh with 308,700 cases reported
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
        metric: exposure
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TC_Megh&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. This layer shows the movement path for 2015
    Tropical Cyclone Megh. Following Tropical Cyclone Chapala, new tropical cyclone
    Megh originated from the Arabian Sea causing even more rains in parts of Bari
    region in Puntland and Somaliland. The storm produced a maximum windspeed of 110knots.
  download_url: null
  format: null
  id: resource_4ced0234
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2015 Tropical Cyclone Megh Path Zipped Shapefile
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TC_Megh&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. This layer shows the movement path for 2015 Tropical Cyclone
    Megh. Following Tropical Cyclone Chapala, new tropical cyclone Megh originated
    from the Arabian Sea causing even more rains in parts of Bari region in Puntland
    and Somaliland. The storm produced a maximum windspeed of 110knots.
  download_url: null
  format: null
  id: resource_0e89e006
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2015 Tropical Cyclone Megh Path CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TC_Megh&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. This layer shows the movement path for 2015 Tropical Cyclone
    Megh. Following Tropical Cyclone Chapala, new tropical cyclone Megh originated
    from the Arabian Sea causing even more rains in parts of Bari region in Puntland
    and Somaliland. The storm produced a maximum windspeed of 110knots.
  download_url: null
  format: null
  id: resource_7352e99b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2015 Tropical Cyclone Megh Path Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TC_Megh&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. This layer shows the movement path for 2015 Tropical
    Cyclone Megh. Following Tropical Cyclone Chapala, new tropical cyclone Megh originated
    from the Arabian Sea causing even more rains in parts of Bari region in Puntland
    and Somaliland. The storm produced a maximum windspeed of 110knots.
  download_url: null
  format: null
  id: resource_f46314b2
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2015 Tropical Cyclone Megh Path GeoJSON
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_icpac_2015tropicalcyclonemeghpa_201511
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
  end: '2015-11-09'
  start: '2015-11-07'
temporal_resolution: null
title: Somalia - 2015 Tropical Cyclone Megh Path
version: null
vulnerability: null
---
