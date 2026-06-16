---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-2010-tropical-cyclone-bandu-path
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-2010-tropical-cyclone-bandu-path
dataset_id: rdls_hl-som_icpac_2010tropicalcyclonebandup_201005
description: 'This layer shows the path followed by Tropical Cyclone Bandu. Early
  on Saturday, 22 May 2010, Tropical Storm 02A moved into the Gulf of Aden and was
  named ''Bandu.'' At that time, Bandu had maximum sustained winds near 45 knots (52
  mph) and was 50 miles north-northwest of Cape Guardafui, Somalia. The storm hit
  Bari Region in northern Somalia, resulting in flooding and displacement of approximately
  12,000 people. TC Bandu quickly dissipated because of cooler waters, higher wind
  shear and drier air in the Gulf of Aden. It curved southwest and made landfall in
  northeast Somalia On May 26, OCHA reported flooding in parts of Belet Weyne town,
  Hiran Region, due to embankment breaches along the Shabelle River as a result of
  2010 TC Bandu, displacing an estimated 17,000 people. According to the FAO Somalia
  Water and Land Information Management Project (SWALIM), flooding also damaged crops
  and resulted in the displacement of a combined population of nearly 2,000 people
  in Jamaame town, Lower Juba Region, as well as Afgooye and Kurtunwaarey districts,
  Lower Shabelle Region.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-2010-tropical-cyclone-bandu-path]'
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
      intensity_measure: vmax:knots
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Observed tropical cyclone track data collected and compiled by ICPAC
    documenting the path, intensity, and meteorological characteristics of Tropical
    Cyclone Bandu as it moved through the Gulf of Aden and made landfall in Somalia
    in May 2010, with associated impact records of displacement and flooding.
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
- href: https://data.humdata.org/dataset/icpac-geonode-2010-tropical-cyclone-bandu-path
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement from Tropical Cyclone Bandu in Somalia
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: vmax:knots
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
    description: Population affected by flooding triggered by Tropical Cyclone Bandu
      in Bari Region, Somalia
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: vmax:knots
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2010_TC_Bandu0&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. This layer shows the path followed by Tropical Cyclone Bandu.
    Early on Saturday, 22 May 2010, Tropical Storm 02A moved into the Gulf of Aden
    and was named 'Bandu.' At that time, Bandu had maximum sustained winds near 45
    knots (52 mph) and was 50 miles north-northwest of Cape Guardafui, Somalia. The
    storm hit Bari Region in northern Somalia, resulting in flooding and displacement
    of approximately 12,000 people. TC Bandu quickly dissipated because of cooler
    waters, higher wind shear and drier air in the Gulf of Aden. It curved southwest
    and made landfall in northeast Somalia
  download_url: null
  format: null
  id: resource_eeaecbaa
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2010 Tropical Cyclone Bandu Path CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2010_TC_Bandu0&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. This layer shows the path followed by Tropical Cyclone
    Bandu. Early on Saturday, 22 May 2010, Tropical Storm 02A moved into the Gulf
    of Aden and was named 'Bandu.' At that time, Bandu had maximum sustained winds
    near 45 knots (52 mph) and was 50 miles north-northwest of Cape Guardafui, Somalia.
    The storm hit Bari Region in northern Somalia, resulting in flooding and displacement
    of approximately 12,000 people. TC Bandu quickly dissipated because of cooler
    waters, higher wind shear and drier air in the Gulf of Aden. It curved southwest
    and made landfall in northeast Somalia
  download_url: null
  format: null
  id: resource_df769aad
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2010 Tropical Cyclone Bandu Path Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2010_TC_Bandu0&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. This layer shows the path followed by Tropical Cyclone
    Bandu. Early on Saturday, 22 May 2010, Tropical Storm 02A moved into the Gulf
    of Aden and was named 'Bandu.' At that time, Bandu had maximum sustained winds
    near 45 knots (52 mph) and was 50 miles north-northwest of Cape Guardafui, Somalia.
    The storm hit Bari Region in northern Somalia, resulting in flooding and displacement
    of approximately 12,000 people. TC Bandu quickly dissipated because of cooler
    waters, higher wind shear and drier air in the Gulf of Aden. It curved southwest
    and made landfall in northeast Somalia
  download_url: null
  format: null
  id: resource_fa561f86
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2010 Tropical Cyclone Bandu Path GeoJSON
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2010_TC_Bandu0&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. This layer shows the path followed by Tropical
    Cyclone Bandu. Early on Saturday, 22 May 2010, Tropical Storm 02A moved into the
    Gulf of Aden and was named 'Bandu.' At that time, Bandu had maximum sustained
    winds near 45 knots (52 mph) and was 50 miles north-northwest of Cape Guardafui,
    Somalia. The storm hit Bari Region in northern Somalia, resulting in flooding
    and displacement of approximately 12,000 people. TC Bandu quickly dissipated because
    of cooler waters, higher wind shear and drier air in the Gulf of Aden. It curved
    southwest and made landfall in northeast Somalia
  download_url: null
  format: null
  id: resource_384d945a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2010 Tropical Cyclone Bandu Path Zipped Shapefile
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_icpac_2010tropicalcyclonebandup_201005
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
title: Somalia - 2010 Tropical Cyclone Bandu Path
version: null
vulnerability: null
---
