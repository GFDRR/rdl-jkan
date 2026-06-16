---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/817
creator:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/817
dataset_id: rdls_hzd-vut_pacificdata_tropicalcyclonelolamodell
description: 'Maximum storm tide around Vanuatu during tropical cyclone Lola simulated
  by the ADCIRC+SWAN coupled hydrodynamic and wave model developed by OPM-SPC for
  the PARTneR-2 project. Water levels are in meters from the mean sea level and account
  for astronomical tide and storm surge (including wave setup but not wave runup).
  This information supports the verification of the cyclone simulation and the timing
  between the astronomical tide and the movement of the cyclone and identifies those
  areas potentially affected by the cyclone''s storm tide. [Source: This metadata
  record was automatically extracted from the GeoNode portal pacificdata]'
details: SPC undertook the rapid coastal inundation assessment based on the first
  available TC vitals after cyclone landfall. Storm surges and waves are simulated
  with the ADCIRC+SWAN coupled wave circulation model (Dietrich et al., 2011), running
  in a non-structured mesh. Atmospheric forcings (i.e., surface pressure and winds)
  are generated with the parametric Dynamic Holland Model (Flemming et al., 2007),
  and tidal forcing along the boundaries comes from TPXO8 (Egbert and Erofeeva, 2002).
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: thunderstorm
      trigger: null
      type: convective_storm
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-NC-SA-4.0
lineage:
  description: This raster map has been produced with the ADCIRC+SWAN modelling suite
    using TPXO 8 to define the astronomical tide and the Dynamical Holland Vortex
    model feed with the official TC track provided by RSMC Fiji to define the meteorological
    forcing (i.e., wind and atmospheric pressure fields).
  sources:
  - id: source_1
    license: null
    name: Earth and Oceans Observations Team Pacific Community
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geonode.pacificdata.org/catalogue/#/dataset/817
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org
purpose: The dataset was developed as part of the PARTneR 2 project, funded by the
  New Zealand Ministry of Foreign Affairs and Trade (MFAT) and was jointly delivered
  by the Pacific Community (SPC) and NIWA, in collaboration with the partner countries.
  It aimed to help countries in the Pacific become more resilient to the impacts of
  climate-related hazards, while building on the pilot PARTneR project, which ran
  from 2016-2019. The project activities included co-developing national risk models
  and assessment tools. The coastal flood bathtub models were developed for Tonga,
  Samoa, Cook Islands, Republic of Marshall Islands, Vanuatu and Tuvalu, based on
  requests from in-country consultations.
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Tropical Cyclone Lola - modelled maximum storm tide_ Vanuatu
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__tc_lola_zeta_max&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  format: null
  id: resource_0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoTIFF
- access_url: https://geonode.pacificdata.org/datasets/geonode:tc_lola_zeta_max
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Tropical Cyclone Lola - modelled maximum storm tide_ Vanuatu (OGC
    WMS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:tc_lola_zeta_max&format=image%2Fpng
  format: null
  id: resource_1
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.pacificdata.org/datasets/geonode:tc_lola_zeta_max
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Tropical Cyclone Lola - modelled maximum storm tide_ Vanuatu (OGC
    WCS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__tc_lola_zeta_max
  format: null
  id: resource_2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WCS: geonode Service'
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-vut_pacificdata_tropicalcyclonelolamodell
spatial:
  bbox:
  - 163.6250322130433
  - -22.31524043182589
  - 173.00746342564005
  - -11.80028843137081
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2024
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Tropical Cyclone Lola - modelled maximum storm tide_ Vanuatu
version: null
vulnerability: null
---
